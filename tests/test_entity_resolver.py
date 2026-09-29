import unittest

from sqlalchemy import create_engine, text

from agent.entity_resolver import EntityResolver, build_entity_aliases
from etl.config import DATABASE_URL


class EntityResolverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        build_entity_aliases(DATABASE_URL)
        cls.resolver = EntityResolver(DATABASE_URL)
        cls.engine = create_engine(DATABASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()
        cls.resolver.engine.dispose()

    def test_client_id_pattern_resolves(self):
        with self.engine.connect() as connection:
            client_id = connection.execute(text(
                "SELECT client_id FROM cleaned.dim_client "
                "WHERE client_id ~ '^[A-Z][0-9]{4,6}$' ORDER BY client_id LIMIT 1"
            )).scalar_one()
        result = self.resolver.resolve(client_id)
        self.assertEqual(result.status, "resolved")
        self.assertEqual(result.resolved.entity_type, "client")
        self.assertEqual(result.resolved.canonical_id, client_id)
        self.assertEqual(result.resolved.method, "id_pattern")

    def test_deal_id_pattern_resolves(self):
        with self.engine.connect() as connection:
            deal_id = connection.execute(text(
                "SELECT deal_id FROM cleaned.dim_deal ORDER BY deal_id LIMIT 1"
            )).scalar_one()
        result = self.resolver.resolve(deal_id)
        self.assertEqual(result.status, "resolved")
        self.assertEqual(result.resolved.entity_type, "deal")
        self.assertEqual(result.resolved.canonical_id, deal_id)

    def test_exact_rm_name_resolves(self):
        with self.engine.connect() as connection:
            rm_name = connection.execute(text(
                "SELECT rm_name FROM cleaned.dim_rm ORDER BY rm_name LIMIT 1"
            )).scalar_one()
        result = self.resolver.resolve(rm_name, "rm")
        self.assertEqual(result.status, "resolved")
        self.assertEqual(result.resolved.canonical_name, rm_name)

    def test_unrecognized_client_is_not_found(self):
        result = self.resolver.resolve("No Such Client 999999", "client")
        self.assertEqual(result.status, "not_found")

    def test_type_hint_is_respected_for_id_patterns(self):
        with self.engine.connect() as connection:
            client_id = connection.execute(text(
                "SELECT client_id FROM cleaned.dim_client "
                "WHERE client_id ~ '^[A-Z][0-9]{4,6}$' ORDER BY client_id LIMIT 1"
            )).scalar_one()
        result = self.resolver.resolve(client_id, "group")
        self.assertNotEqual(result.status, "resolved")


if __name__ == "__main__":
    unittest.main()