# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LocalizaArticulo(models.Model):
    _name = 'localiza.articulo'
    _description = 'Artículo operativo de bodega'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'categoria, name'

    name = fields.Char(string='Nombre', required=True, tracking=True)
    codigo = fields.Char(string='Código interno', index=True, tracking=True)
    categoria = fields.Selection([
        ('uniforme', 'Uniforme'),
        ('insumo', 'Insumo'),
        ('gps', 'GPS'),
        ('herramienta', 'Herramienta'),
        ('equipo_industrial', 'Equipo industrial'),
        ('vehiculo', 'Vehículo'),
        ('otro', 'Otro'),
    ], string='Categoría', default='insumo', required=True, tracking=True)
    subcategoria = fields.Char(string='Subcategoría')
    product_id = fields.Many2one('product.product', string='Producto Odoo relacionado')
    talla = fields.Char(string='Talla / medida')
    unidad = fields.Char(string='Unidad', default='Unidad')
    requiere_serie = fields.Boolean(string='Requiere serie / código único')
    stock_minimo = fields.Float(string='Stock mínimo')
    criticidad = fields.Selection([
        ('normal', 'Normal'),
        ('controlado', 'Controlado'),
        ('critico', 'Crítico'),
    ], string='Criticidad', default='normal')
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notas')

    _sql_constraints = [
        ('codigo_unique', 'unique(codigo)', 'El código interno del artículo ya existe.'),
    ]

    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            if rec.product_id:
                if not rec.name:
                    rec.name = rec.product_id.display_name
                if not rec.codigo:
                    rec.codigo = rec.product_id.default_code
