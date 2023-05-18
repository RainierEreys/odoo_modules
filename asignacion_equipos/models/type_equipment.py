# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class TypeEquipment(models.Model):
    _name = 'type.equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Nombre de equipo', required=True,)
    date_create = fields.Date('Fecha de creacion', default=date.today())
    codigo = fields.Char('Codigo', required=True, copy=False, default='Cod')
    #CONDICIONAR EL CAMPO 'codigo' PARA QUE ESTE SEA UNICO
    _sql_constraints = [('codigo_unico', 'unique(codigo)', 'El código ya existe en el registro')]
    #ASIGNACION DE SECUENCIA (SE UTILIZA EL MODELO 'ir.sequence')
    @api.model
    def create(self, vals):
        if vals.get('codigo', 'Cod') == 'Cod':
            vals['codigo'] = self.env['ir.sequence'].next_by_code('type.equipment') or u'Cod'
            result = super(TypeEquipment, self).create(vals)

            return result
        