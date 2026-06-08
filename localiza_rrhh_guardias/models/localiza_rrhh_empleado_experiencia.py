# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhEmpleadoExperiencia(models.Model):
    _name = "localiza.rrhh.empleado.experiencia"
    _description = "hr_employee_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    currency = fields.Many2one("res.currency", string="Currency", ondelete="set null")
    x_hr_employee = fields.Many2one("hr.employee", string="X Hr Employee", ondelete="set null")
    name = fields.Char(string="Compañía que laboro")
    jefe_inmediato = fields.Char(string="Jefe inmediato")
    currency_2 = fields.Many2one("res.currency", string="Currency", ondelete="set null")
    motivo_de_retiro = fields.Char(string="Motivo de retiro")
    puesto = fields.Char(string="Puesto ")
    salario = fields.Float(string="Salario: ")
    salario_2 = fields.Float(string="Salario")
    sequence = fields.Integer(string="Secuencia")
    telefono = fields.Char(string="Teléfono")
    telefono_de_contacto = fields.Char(string="Teléfono de contacto")
    tiempo_laborado = fields.Char(string="Tiempo laborado")
    active = fields.Boolean(string="Activo", default=True)
