# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaRrhhPlanillaPago(models.Model):
    _name = "localiza.rrhh.planilla.pago"
    _description = "Planilla de Pagos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    fecha = fields.Date(string="Fecha ")
    recibo_de_nomina = fields.Many2many("hr.payslip", string="Recibo de nómina")
    regla_salarial = fields.Many2one("hr.salary.rule", string="Regla salarial", ondelete="set null")
    entrada_de_recibo_de_nomina = fields.Many2one("hr.payslip.input", string="Entrada de recibo de nómina", ondelete="set null")
    empleado = fields.Many2one("hr.employee", string="Empleado", ondelete="set null")
    sequence = fields.Integer(string="Secuencia")
