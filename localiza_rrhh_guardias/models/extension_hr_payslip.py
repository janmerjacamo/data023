# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaExtHr_payslip(models.Model):
    _inherit = "hr.payslip"

    new_campo_relacionado = fields.Char(string="New Campo relacionado")
    new_campo_relacionado_2 = fields.Char(string="New Campo relacionado")
    new_campo_relacionado_3 = fields.Char(string="New Campo relacionado", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    new_campo_relacionado_4 = fields.Many2one("hr.salary.rule.category", string="New Campo relacionado", ondelete="set null")
