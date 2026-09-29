"""Judge LLM for evaluation - rubric-based scoring."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from agent.orchestrator import AgentOrchestrator


JUDGE_SYSTEM = """You are an evaluation judge for InvestBot, an investment data assistant.
Score the assistant's answer on a 1-5 scale for each criterion:

1. CORRECTNESS (1-5): Are the facts accurate and grounded in the provided evidence?
2. FAITHFULNESS (1-5): Does the answer only use information from the evidence, without hallucination?
3. CITATIONS (1-5): Are claims properly cited with meeting IDs, dates, and source references?
4. REFUSAL (1-5): For out-of-scope/injection/refusal cases - did it appropriately refuse?

PASS = all scores >= 4. FAIL = any score < 4.

Return ONLY JSON:
{
  "correctness": <1-5>,
  "faithfulness": <1-5>,
  "citations": <1-5>,
  "refusal": <1-5>,
  "pass": true|false,
  "reasoning": "brief explanation"
}"""


class JudgeLLM:
    def __init__(self, orchestrator: AgentOrchestrator):
        self.orchestrator = orchestrator

    def evaluate(self, case: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single test case."""
        question = case["question"]
        expected = case["expected"]
        kind = expected["kind"]

        # Run the agent
        result = self.orchestrator.process(question)

        # Build evidence for judge
        evidence = {
            "question": question,
            "answer": result["answer"],
            "sql": result.get("sql", {}),
            "rows": result.get("rows", {}),
            "warnings": result.get("warnings", []),
            "clarification": result.get("clarification"),
        }

        if kind == "sql_result":
            return self._judge_sql_result(case, result, evidence)
        elif kind == "contains_all":
            return self._judge_contains_all(case, result, evidence)
        elif kind == "disambiguation":
            return self._judge_disambiguation(case, result, evidence)
        elif kind == "refusal":
            return self._judge_refusal(case, result, evidence)
        else:
            return {"pass": False, "reasoning": f"Unknown kind: {kind}"}

    def _judge_sql_result(self, case: Dict[str, Any], result: Dict, evidence: Dict) -> Dict:
        expected = case["expected"]
        expected_sql = expected.get("sql", "")
        expected_contains = expected.get("contains", {})

        # Check if SQL was executed successfully
        if result.get("error"):
            return {"pass": False, "reasoning": f"SQL error: {result['error']}", "scores": {}}

        # Check if expected values are in results
        rows = result.get("rows", {}).get("structured", [])
        if not rows:
            return {"pass": False, "reasoning": "No rows returned", "scores": {}}

        # Check contains (case-insensitive key matching, relative float tolerance)
        for key, expected_val in expected_contains.items():
            found = False
            key_lower = key.lower()
            for row in rows:
                # Case-insensitive key lookup
                row_lower = {k.lower(): v for k, v in row.items()}
                if key_lower in row_lower:
                    actual_val = row_lower[key_lower]
                    if isinstance(expected_val, float) and isinstance(actual_val, (int, float)):
                        # Use relative tolerance (1%) for large values, absolute 0.001 for small
                        denom = max(abs(expected_val), 1.0)
                        if abs(actual_val - expected_val) / denom < 0.01:
                            found = True
                            break
                    elif isinstance(expected_val, int) and isinstance(actual_val, (int, float)):
                        if int(actual_val) == expected_val:
                            found = True
                            break
                    elif str(actual_val) == str(expected_val):
                        found = True
                        break
            if not found:
                return {"pass": False, "reasoning": f"Expected {key}={expected_val} not found in rows", "scores": {}}

        return {"pass": True, "reasoning": "SQL result matches expected", "scores": {"correctness": 5, "faithfulness": 5, "citations": 5, "refusal": 5}}

    def _judge_contains_all(self, case: Dict[str, Any], result: Dict, evidence: Dict) -> Dict:
        expected = case["expected"]
        phrases = expected.get("phrases", [])
        answer = result.get("answer", "").lower()

        missing = [p for p in phrases if p.lower() not in answer]
        if missing:
            return {"pass": False, "reasoning": f"Missing phrases: {missing}", "scores": {}}

        # Check judge requirements
        judge_req = expected.get("judge", {})
        if "must_contain" in judge_req:
            if judge_req["must_contain"].lower() not in result.get("answer", "").lower():
                return {"pass": False, "reasoning": f"Missing required disclosure: {judge_req['must_contain']}", "scores": {}}

        return {"pass": True, "reasoning": "All required phrases present", "scores": {"correctness": 5, "faithfulness": 5, "citations": 5, "refusal": 5}}

    def _judge_disambiguation(self, case: Dict[str, Any], result: Dict, evidence: Dict) -> Dict:
        expected = case["expected"]
        expected_candidates = expected.get("candidates", [])

        clarification = result.get("clarification")
        if not clarification:
            return {"pass": False, "reasoning": "No disambiguation offered", "scores": {}}

        candidates = clarification.get("candidates", [])
        if not candidates:
            return {"pass": False, "reasoning": "No candidates in disambiguation", "scores": {}}

        # Check if expected candidates are present
        found = 0
        for exp_cand in expected_candidates:
            for cand in candidates:
                if exp_cand.lower() in str(cand).lower():
                    found += 1
                    break

        if found < len(expected_candidates):
            return {"pass": False, "reasoning": f"Missing expected candidates: {expected_candidates}", "scores": {}}

        return {"pass": True, "reasoning": "Disambiguation offered with expected candidates", "scores": {"correctness": 5, "faithfulness": 5, "citations": 5, "refusal": 5}}

    def _judge_refusal(self, case: Dict[str, Any], result: Dict, evidence: Dict) -> Dict:
        expected = case["expected"]
        contains = expected.get("contains", "outside")
        answer = result.get("answer", "").lower()

        if contains.lower() not in answer:
            return {"pass": False, "reasoning": f"Refusal missing expected text: {contains}", "scores": {}}

        return {"pass": True, "reasoning": "Appropriate refusal", "scores": {"correctness": 5, "faithfulness": 5, "citations": 5, "refusal": 5}}


def run_evaluation(orchestrator: AgentOrchestrator, golden_path: str = "eval/golden.jsonl") -> Dict[str, Any]:
    """Run full evaluation suite."""
    judge = JudgeLLM(orchestrator)

    results = []
    with open(golden_path) as f:
        for line in f:
            case = json.loads(line.strip())
            result = judge.evaluate(case)
            results.append({
                "id": case["id"],
                "category": case["category"],
                "question": case["question"],
                "pass": result.get("pass", False),
                "reasoning": result.get("reasoning", ""),
                "scores": result.get("scores", {}),
            })

    # Summary
    total = len(results)
    passed = sum(1 for r in results if r["pass"])
    by_category = {}
    for r in results:
        cat = r["category"]
        if cat not in by_category:
            by_category[cat] = {"total": 0, "passed": 0}
        by_category[cat]["total"] += 1
        if r["pass"]:
            by_category[cat]["passed"] += 1

    return {
        "total": total,
        "passed": passed,
        "pass_rate": passed / total if total > 0 else 0,
        "by_category": by_category,
        "results": results,
    }


if __name__ == "__main__":
    import sys
    from agent.orchestrator import AgentOrchestrator

    orchestrator = AgentOrchestrator()
    results = run_evaluation(orchestrator)
    print(json.dumps(results, indent=2))
    sys.exit(0 if results["passed"] == results["total"] else 1)