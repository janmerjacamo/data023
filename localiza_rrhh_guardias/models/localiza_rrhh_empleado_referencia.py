# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoReferencia(models.Model):
    _name = "localiza.rrhh.empleado.referencia"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Nombre:")
    parentesco = fields.Char(string="Parentesco:")
    sequence = fields.Integer(string="Secuencia")
    telefono = fields.Char(string="Teléfono:")
    active = fields.Boolean(string="Activo", default=True)
