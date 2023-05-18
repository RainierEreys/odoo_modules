# -*- coding: utf-8 -*-
# from odoo import http


# class AsignacionEquipos(http.Controller):
#     @http.route('/asignacion_equipos/asignacion_equipos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asignacion_equipos/asignacion_equipos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asignacion_equipos.listing', {
#             'root': '/asignacion_equipos/asignacion_equipos',
#             'objects': http.request.env['asignacion_equipos.asignacion_equipos'].search([]),
#         })

#     @http.route('/asignacion_equipos/asignacion_equipos/objects/<model("asignacion_equipos.asignacion_equipos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asignacion_equipos.object', {
#             'object': obj
#         })
