# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaExtAccount_move(models.Model):
    _inherit = "account.move"

    codigo_sem = fields.Char(string="CODIGO SEM")
    liquidacion = fields.Many2one("localiza.liquidacion", string="LIQUIDACION", ondelete="set null")
    no_docto = fields.Char(string="No./Docto.")
    serie = fields.Char(string="Serie")
