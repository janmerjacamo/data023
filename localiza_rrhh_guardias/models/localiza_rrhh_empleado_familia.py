# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoFamilia(models.Model):
    _name = "localiza.rrhh.empleado.familia"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Núcleo Familiar")
    apellidos = fields.Char(string="Apellidos")
    n = fields.Integer(string="N°")
    nombres = fields.Char(string="Nombres")
    sequence = fields.Integer(string="Secuencia")
    telefono_celular = fields.Char(string="Teléfono Celular")
    active = fields.Boolean(string="Activo", default=True)
