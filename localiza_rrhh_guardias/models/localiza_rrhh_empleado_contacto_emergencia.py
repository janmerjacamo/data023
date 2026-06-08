# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoContactoEmergencia(models.Model):
    _name = "localiza.rrhh.empleado.contacto.emergencia"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Nombre")
    parentesco = fields.Char(string="Parentesco")
    sequence = fields.Integer(string="Secuencia")
    telefono_celular = fields.Char(string="Teléfono Celular")
    active = fields.Boolean(string="Activo", default=True)
