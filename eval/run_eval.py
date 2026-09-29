#!/usr/bin/env python3
"""Run evaluation suite for InvestBot."""

import sys
import json
from eval.judge import run_evaluation
from agent.orchestrator import AgentOrchestrator


def main():
    orchestrator = AgentOrchestrator()
    results = run_evaluation(orchestrator)
    
    print(f"\n{'='*60}")
    print(f"EVALUATION RESULTS")
    print(f"{'='*60}")
    print(f"Total: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Pass Rate: {results['pass_rate']:.1%}")
    print()
    
    for cat, stats in results["by_category"].items():
        rate = stats["passed"] / stats["total"] if stats["total"] > 0 else 0
        print(f"  {cat}: {stats['passed']}/{stats['total']} ({rate:.1%})")
    
    print()
    for r in results["results"]:
        status = "PASS" if r["pass"] else "FAIL"
        print(f"  [{status}] {r['id']} ({r['category']}): {r['question'][:60]}...")
        if not r["pass"]:
            print(f"    Reason: {r['reasoning']}")
    
    print(f"\n{'='*60}")
    if results["passed"] == results["total"]:
        print("ALL TESTS PASSED")
        sys.exit(0)
    else:
        print(f"FAILED: {results['total'] - results['passed']} tests failed")
        sys.exit(1)


if __name__ == "__main__":
    main()