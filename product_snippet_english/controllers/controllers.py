# -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request

# class ProductSnippetEnglish(http.Controller):
#     @http.route('/product_snippet_english/cart_content', type="json", auth='public', website=True)
#     def cart(self):
#         products = request.website.sale_get_order().order_line.product_id
#         data = []
#         for product in products:
#             fields = product.read(['display_name', 'description_sale', 'list_price', 'website_url'])[0];
#             fields['image'] = request.env['website'].image_url(product, 'image_512')
#             data.append(fields)
#         return request.env['ir.ui.view']._render_template('custom_snippets.s_cart_products_card', {'products': data})

# class ProductSnippetEnglish(http.Controller):
#     @http.route('/product_snippet_english/product_snippet_english/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_snippet_english/product_snippet_english/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_snippet_english.listing', {
#             'root': '/product_snippet_english/product_snippet_english',
#             'objects': http.request.env['product_snippet_english.product_snippet_english'].search([]),
#         })

#     @http.route('/product_snippet_english/product_snippet_english/objects/<model("product_snippet_english.product_snippet_english"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_snippet_english.object', {
#             'object': obj
#         })
