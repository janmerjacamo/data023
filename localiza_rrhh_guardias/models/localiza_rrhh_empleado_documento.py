# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoDocumento(models.Model):
    _name = "localiza.rrhh.empleado.documento"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    empleado = fields.Many2one("hr.employee", string="Empleado", ondelete="set null")
    name = fields.Char(string="Número de Serie")
    fecha_de_emision = fields.Date(string="Fecha de Emisión ")
    fecha_de_vencimiento = fields.Date(string="Fecha de Vencimiento")
    usuario = fields.Many2one("res.users", string="Usuario", ondelete="set null")
    empleado_2 = fields.Many2one("hr.employee", string="Empleado", ondelete="set null")
    nombre_del_archivo = fields.Binary(string="Nombre del Archivo")
    filename_for_binary_field_lg2z9 = fields.Char(string="Filename for x_studio_binary_field_Lg2Z9")
    sequence = fields.Integer(string="Secuencia")
    tipo_de_documento = fields.Char(string="Tipo de Documento")
    active = fields.Boolean(string="Activo", default=True)
