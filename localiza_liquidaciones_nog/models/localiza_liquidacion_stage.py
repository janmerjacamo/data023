# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaLiquidacionStage(models.Model):
    _name = "localiza.liquidacion.stage"
    _description = "LIQUIDACION Stages"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre de la etapa")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
