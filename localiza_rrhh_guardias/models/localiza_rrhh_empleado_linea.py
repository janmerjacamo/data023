# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoLinea(models.Model):
    _name = "localiza.rrhh.empleado.linea"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Descripción")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
