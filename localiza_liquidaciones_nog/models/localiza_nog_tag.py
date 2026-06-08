# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaNogTag(models.Model):
    _name = "localiza.nog.tag"
    _description = "NOG Tags"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    color = fields.Integer(string="Color")
    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=10)
