# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTecnico(models.Model):
    _name = "localiza.tecnico"
    _description = "Técnicos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    aplica_para_formulario = fields.Boolean(string="APLICA PARA FORMULARIO")
    sequence = fields.Integer(string="Secuencia")
