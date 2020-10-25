from odoo.tests.common import TransactionCase


class TestCase(TransactionCase):
    def test_compute(self):
        record = self.env["test.case"].create({"name": "test", "value": 3, "value2": 2})
        record.compute()
        self.assertEqual(record.result, 9)
