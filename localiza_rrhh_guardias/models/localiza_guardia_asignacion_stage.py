# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaGuardiaAsignacionStage(models.Model):
    _name = "localiza.guardia.asignacion.stage"
    _description = "Guardias Asignación Puesto Stages"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre de la etapa")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
