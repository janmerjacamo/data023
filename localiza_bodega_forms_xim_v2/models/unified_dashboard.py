from odoo import fields, models


class LocalizaBodegaDashboardCard(models.Model):
    _name = 'localiza.bodega.dashboard.card'
    _description = 'Panel principal unificado de bodega'
    _order = 'sequence, id'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    card_type = fields.Selection([
        ('formularios', 'Formularios'),
        ('entregas', 'Entregas'),
        ('puestos', 'Puestos'),
        ('gps', 'GPS'),
        ('articulos', 'Artículos'),
        ('prestamos', 'Préstamos'),
        ('inventarios', 'Inventarios de puesto'),
        ('instalaciones', 'Instalaciones'),
    ], required=True, default='formularios')
    description = fields.Char()
    color = fields.Integer(default=0)
    total_count = fields.Integer(compute='_compute_counts')
    pending_count = fields.Integer(compute='_compute_counts')
    done_count = fields.Integer(compute='_compute_counts')
    alert_count = fields.Integer(compute='_compute_counts')

    def _compute_counts(self):
        Form = self.env['localiza.forms.operation']
        Entrega = self.env['localiza.entrega']
        Puesto = self.env['localiza.puesto']
        GPS = self.env['localiza.gps.equipo']
        Art = self.env['localiza.articulo']
        for rec in self:
            rec.total_count = 0
            rec.pending_count = 0
            rec.done_count = 0
            rec.alert_count = 0
            if rec.card_type == 'formularios':
                rec.total_count = Form.search_count([])
                rec.pending_count = Form.search_count([('state', '=', 'draft')])
                rec.done_count = Form.search_count([('state', 'in', ['validated', 'closed'])])
                rec.alert_count = Form.search_count([('state', '=', 'cancelled')])
            elif rec.card_type == 'entregas':
                rec.total_count = Entrega.search_count([])
                rec.pending_count = Entrega.search_count([('state', 'in', ['draft', 'confirmed'])])
                rec.done_count = Entrega.search_count([('state', '=', 'done')])
                rec.alert_count = Entrega.search_count([('state', '=', 'cancel')])
            elif rec.card_type == 'puestos':
                rec.total_count = Puesto.search_count([])
                rec.pending_count = Puesto.search_count([('state', '=', 'baja')])
                rec.done_count = Puesto.search_count([('state', '=', 'alta')])
                rec.alert_count = Puesto.search_count([('active', '=', False)])
            elif rec.card_type == 'gps':
                rec.total_count = GPS.search_count([])
                rec.pending_count = GPS.search_count([('state', '=', 'bodega')])
                rec.done_count = GPS.search_count([('state', 'in', ['asignado', 'instalado'])])
                rec.alert_count = GPS.search_count([('state', 'in', ['danado', 'perdido'])])
            elif rec.card_type == 'articulos':
                rec.total_count = Art.search_count([])
                rec.pending_count = Art.search_count([('criticidad', '=', 'controlado')])
                rec.done_count = Art.search_count([('active', '=', True)])
                rec.alert_count = Art.search_count([('criticidad', '=', 'critico')])
            elif rec.card_type == 'prestamos':
                dom = [('form_type', '=', 'prestamo_herramientas')]
                rec.total_count = Form.search_count(dom)
                rec.pending_count = Form.search_count(dom + [('state', '=', 'draft')])
                rec.done_count = Form.search_count(dom + [('state', 'in', ['validated', 'closed'])])
                rec.alert_count = Form.search_count(dom + [('state', '=', 'cancelled')])
            elif rec.card_type == 'inventarios':
                dom = [('form_type', '=', 'inventario_puesto')]
                rec.total_count = Form.search_count(dom)
                rec.pending_count = Form.search_count(dom + [('state', '=', 'draft')])
                rec.done_count = Form.search_count(dom + [('state', 'in', ['validated', 'closed'])])
                rec.alert_count = Form.search_count(dom + [('state', '=', 'cancelled')])
            elif rec.card_type == 'instalaciones':
                dom = [('form_type', '=', 'instalacion_puesto')]
                rec.total_count = Form.search_count(dom)
                rec.pending_count = Form.search_count(dom + [('state', '=', 'draft')])
                rec.done_count = Form.search_count(dom + [('state', 'in', ['validated', 'closed'])])
                rec.alert_count = Form.search_count(dom + [('state', '=', 'cancelled')])

    def _action_for_card(self, pending=False):
        self.ensure_one()
        if self.card_type == 'entregas':
            domain = [('state', 'in', ['draft', 'confirmed'])] if pending else []
            return {'type': 'ir.actions.act_window', 'name': self.name, 'res_model': 'localiza.entrega', 'view_mode': 'kanban,list,form', 'domain': domain}
        if self.card_type == 'puestos':
            domain = [('state', '=', 'baja')] if pending else []
            return {'type': 'ir.actions.act_window', 'name': self.name, 'res_model': 'localiza.puesto', 'view_mode': 'list,form', 'domain': domain}
        if self.card_type == 'gps':
            domain = [('state', '=', 'bodega')] if pending else []
            return {'type': 'ir.actions.act_window', 'name': self.name, 'res_model': 'localiza.gps.equipo', 'view_mode': 'list,form', 'domain': domain}
        if self.card_type == 'articulos':
            domain = [('criticidad', 'in', ['controlado', 'critico'])] if pending else []
            return {'type': 'ir.actions.act_window', 'name': self.name, 'res_model': 'localiza.articulo', 'view_mode': 'list,form', 'domain': domain}
        domain = []
        ctx = {}
        if self.card_type == 'prestamos':
            domain = [('form_type', '=', 'prestamo_herramientas')]
            ctx = {'default_form_type': 'prestamo_herramientas'}
        elif self.card_type == 'inventarios':
            domain = [('form_type', '=', 'inventario_puesto')]
            ctx = {'default_form_type': 'inventario_puesto'}
        elif self.card_type == 'instalaciones':
            domain = [('form_type', '=', 'instalacion_puesto')]
            ctx = {'default_form_type': 'instalacion_puesto'}
        if pending:
            domain = domain + [('state', '=', 'draft')]
        return {'type': 'ir.actions.act_window', 'name': self.name, 'res_model': 'localiza.forms.operation', 'view_mode': 'list,form', 'domain': domain, 'context': ctx}

    def action_open(self):
        return self._action_for_card(False)

    def action_open_pending(self):
        return self._action_for_card(True)
