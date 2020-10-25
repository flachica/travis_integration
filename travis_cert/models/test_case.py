from odoo import fields, models


class TestCase(models.Model):
    _name = "test.case"
    _description = "Testing cases"

    name = fields.Char()
    value = fields.Integer("Value 1")
    value2 = fields.Integer("Value 2")
    result = fields.Integer("Result")

    def compute(self):
        self.ensure_one()
        self.result = self.value * self.value2
