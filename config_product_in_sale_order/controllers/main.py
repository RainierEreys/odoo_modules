from odoo import http, tools
from odoo.http import request
import logging
logger = logging.getLogger(__name__)

class WebsiteMathdata(http.Controller):
    
    @http.route("/autocomplete/", auth='user', website=True)
    def render_dashboard(self, **kw):
        
        return 'Autocomplete'        
    
    @http.route("/config_product_user", type="http", auth='user', website=True)
    def panel_configuracion(self, **kw):
        user_id = http.request.env['res.users'].browse(http.request.env.context.get('uid')) if http.request.env.context.get('uid', False) else False
        product_paths = user_id.sudo().get_all_products_available()        
        subscription = http.request.env['sale.order'].sudo().search([('partner_id', '=', user_id.partner_id.id), ('stage_id', '=', 'En progreso')])        
        if subscription:
            verify = True
        else:
            verify = False
        logger.info(verify)

        return http.request.render("config_product_in_sale_order.configurador_product", {'products': product_paths, 'verify': verify})