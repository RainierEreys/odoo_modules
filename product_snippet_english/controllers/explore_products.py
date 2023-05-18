# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
#CONSULTA DE INFORMACIÓN EN BDD (MODELOS 'res.users', 'res.partner' y 'product.template')
class YourHomeCities(http.Controller):
    
    @http.route('/get_normalproducts/', auth="public", type="json", methods=['POST'])
    def all_cities(self):
        data = []
        
        
        type_user = http.request.env['res.users'].sudo().search_read([], ['name'])
        info_contact = http.request.env['res.partner'].sudo().search_read([], ['name', 'image_1920', 'email'])
        product = http.request.env['product.template'].sudo().search_read([], ['type', 'name', 'image_1920', 'website_url'], limit=10)
        contacto2 = http.request.env['res.partner'].sudo().read(['name'])
        
        
        return {'type_user' : type_user, 'product' : product, 'contacto' : info_contact, 'numero' : numero, 'contacto2' : contacto2}