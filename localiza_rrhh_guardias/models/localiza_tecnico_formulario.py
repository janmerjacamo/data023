# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTecnicoFormulario(models.Model):
    _name = "localiza.tecnico.formulario"
    _description = "Formulario Técnicos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    apagado = fields.Char(string="APAGADO", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    estado = fields.Char(string="ESTADO", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    icc = fields.Char(string="ICC")
    imei = fields.Char(string="IMEI")
    modelo = fields.Many2one("localiza.equipo.modelo", string="MODELO", ondelete="set null")
    no_orden = fields.Char(string="NO. ORDEN")
    no_serie = fields.Char(string="NO. SERIE")
    revisado = fields.Char(string="Revisado ", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    sequence = fields.Integer(string="Secuencia")
    sim = fields.Char(string="SIM")
    tamper = fields.Char(string="TAMPER", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    tecnico = fields.Many2one("localiza.tecnico", string="TECNICO", ondelete="set null")
    tipo_de_servicios = fields.Many2one("localiza.servicio.tipo", string="TIPO DE SERVICIOS", ondelete="set null")
