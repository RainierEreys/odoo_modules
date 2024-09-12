# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = "practice_module.visit"
    _description = "visita"

    name = fields.Char(string='Description')
    customer = fields.Char(string='Cliente')
    date = fields.Datetime(string="Fecha")
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telfonico')], string="Tipo", required=True)
    done = fields.Boolean(string="realizada", readonly="True")

