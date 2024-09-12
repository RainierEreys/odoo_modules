# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    def get_partner_id(self):
        return self.sudo().partner_id.id
    
    def get_all_products_available(self):
        product_template_model = self.env['product.template']                
        published_products = product_template_model.search([('website_published', '=', True)])             
        products = []
        for line in published_products:
            products.append({
                'product_id': str(line.id),
                'product_name': line.name,
                'product_price': line.list_price,                
                'image':'{url_base}/web/image/product.product/{id}/image_1920'.format(url_base=self.env['ir.config_parameter'].sudo().get_param('web.base.url'),id=line.id)                               
            })                    
        return products
        
        # paths = []
        # line_product = []
        # if sale_ids:
        #     for line in sale_ids.order_line:
        #         if line.product_id and line.product_id.detailed_type == 'service' and line.product_id.path_website_page and line.product_id.path_website_page.replace(' ','') not in ('',False,None):
        #             line_product.append({
        #                 'product_id':line.product_id.id,
        #                 'product_name':line.product_id.name,
        #                 'path':line.product_id.path_website_page.replace(' ',''),
        #                 'image':'{url_base}/web/image/product.product/{id}/image_1920'.format(url_base=self.env['ir.config_parameter'].sudo().get_param('web.base.url'),id=line.product_id.id)
        #             })
        #         if len(line_product) >= 3:
        #             paths.append(line_product)
        #             line_product = []
        #     paths.append(line_product)
        # return paths