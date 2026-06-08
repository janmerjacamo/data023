# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaNogEstatus(models.Model):
    _name = "localiza.nog.estatus"
    _description = "Estatus de NOG"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    sequence = fields.Integer(string="Secuencia")
    estatus_count = fields.Integer(string="Estatus count")
