# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoEstudio(models.Model):
    _name = "localiza.rrhh.empleado.estudio"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Nivel Educativo")
    archivo = fields.Binary(string="Archivo")
    filename_for_binary_field_7j6l0 = fields.Char(string="Filename for x_studio_binary_field_7j6L0")
    centro = fields.Char(string="Centro")
    grado_academico = fields.Char(string="Grado Académico ")
    no = fields.Integer(string="No.")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
