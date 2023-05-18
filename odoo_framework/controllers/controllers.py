# -*- coding: utf-8 -*-
# from odoo import http


# class OdooFramework(http.Controller):
#     @http.route('/odoo_framework/odoo_framework/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_framework/odoo_framework/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_framework.listing', {
#             'root': '/odoo_framework/odoo_framework',
#             'objects': http.request.env['odoo_framework.odoo_framework'].search([]),
#         })

#     @http.route('/odoo_framework/odoo_framework/objects/<model("odoo_framework.odoo_framework"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_framework.object', {
#             'object': obj
#         })
