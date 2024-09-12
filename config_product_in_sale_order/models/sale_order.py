# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def create_sale_order_config(self, product_ids):  
        self = self.sudo()
        order = self.env['sale.order'].create({
            'partner_id': self.id,
            # Otros campos relevantes según tus necesidades
        })           
        logger.info(order.id)
        for product_id in product_ids:            
            product = self.env['product.template'].browse(product_id)            
            order_line_vals = {
                'order_id': order.id,
                'product_id':product.id,
                'product_template_id': product.id,
                'product_uom_qty': 1, 
                'name': product.name,
                'price_unit': product.list_price,
                # Otros campos relevantes según tus necesidades
            }
            self.env['sale.order.line'].create(order_line_vals)

        return order