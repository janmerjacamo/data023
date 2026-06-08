# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaLiquidacion(models.Model):
    _name = "localiza.liquidacion"
    _description = "LIQUIDACION"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    avatar = fields.Binary(string="Avatar")
    color = fields.Integer(string="Color")
    moneda = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    name = fields.Char(string="Descripción")
    aguinaldo = fields.Float(string="Aguinaldo")
    bono_14 = fields.Float(string="Bono 14")
    moneda_2 = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    dias_pendientes_de_pago = fields.Integer(string="Días pendientes de pago:")
    fecha = fields.Date(string="Fecha")
    dpi = fields.Integer(string="DPI:")
    horas_extras_pendientes = fields.Integer(string="Horas extras pendientes: ")
    igss = fields.Float(string="IGSS")
    igss_p = fields.Float(string="IGSS P")
    indemnizacion = fields.Float(string="Indemnización")
    ingreso = fields.Date(string="Ingreso:")
    estado_de_kanban = fields.Char(string="Estado de kanban", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    empleado = fields.Many2one("hr.employee", string="Empleado", ondelete="set null")
    asiento_contable = fields.Many2one("account.move", string="Asiento contable", ondelete="set null")
    motivo = fields.Char(string="Motivo:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    n_de_dpi = fields.Char(string="N° de DPI:")
    nombre_del_puesto = fields.Char(string="Nombre del puesto:")
    correo_electronico = fields.Char(string="Correo electrónico")
    contacto = fields.Many2one("res.partner", string="Contacto", ondelete="set null")
    telefono = fields.Char(string="Teléfono")
    alta_prioridad = fields.Boolean(string="Alta Prioridad")
    publicar_registro_contable = fields.Boolean(string="Publicar Registro Contable: ")
    puesto = fields.Char(string="Puesto:")
    new_campo_relacionado = fields.Integer(string="New Campo relacionado")
    salario_promedio = fields.Float(string="Salario Promedio:")
    salida = fields.Date(string="Salida:")
    salida_2 = fields.Date(string="Salida:")
    sequence = fields.Integer(string="Secuencia")
    etapa = fields.Many2one("localiza.liquidacion.stage", string="Etapa", ondelete="set null")
    etiquetas = fields.Many2many("localiza.liquidacion.tag", string="Etiquetas")
    total_a_liquidar = fields.Float(string="Total a Liquidar")
    total_dias_laborados = fields.Integer(string="Total días laborados:")
    total_liquido_a_recibir = fields.Float(string="Total Liquido a Recibir")
    vacaciones = fields.Float(string="Vacaciones")
    valor = fields.Float(string="Valor")
