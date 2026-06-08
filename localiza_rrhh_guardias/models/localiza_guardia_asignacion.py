# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaGuardiaAsignacion(models.Model):
    _name = "localiza.guardia.asignacion"
    _description = "Guardias Localiza"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    color = fields.Integer(string="Color")
    name = fields.Char(string="Descripción")
    estado = fields.Char(string="Estado", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    fecha_de_registro = fields.Date(string="Fecha de Registro")
    estado_de_kanban = fields.Char(string="Estado de kanban", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    empleado = fields.Many2one("hr.employee", string="Empleado", ondelete="set null")
    puestos_guardias = fields.Many2one("localiza.guardia.puesto", string="Puestos Guardias", ondelete="set null")
    turnos_de_guardias = fields.Many2one("localiza.guardia.turno", string="Turnos de guardias", ondelete="set null")
    alta_prioridad = fields.Boolean(string="Alta Prioridad")
    sequence = fields.Integer(string="Secuencia")
    etapa = fields.Many2one("localiza.guardia.asignacion.stage", string="Etapa", ondelete="set null")
    responsable = fields.Many2one("res.users", string="Responsable", ondelete="set null")
