# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaGuardiaPuesto(models.Model):
    _name = "localiza.guardia.puesto"
    _description = "Puestos Guardias"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    avatar = fields.Binary(string="Avatar")
    name = fields.Char(string="Descripción")
    area_de_puesto = fields.Char(string="Area de Puesto ", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    descripcion_del_puesto = fields.Char(string="Descripción del Puesto")
    turnos_de_guardias = fields.Many2many("localiza.guardia.turno", string="Turnos de guardias")
    guardias_localiza = fields.Many2many("localiza.guardia.asignacion", string="Guardias Localiza")
    n_de_guardias = fields.Integer(string="N° de Guardias")
    # new_unoamuchos: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    pipeline_status_bar = fields.Char(string="Pipeline status bar", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    sequence = fields.Integer(string="Secuencia")
    ubicacion_del_puesto = fields.Char(string="Ubicación del Puesto")
