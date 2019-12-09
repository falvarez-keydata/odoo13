# -*- coding: utf-8 -*-
# from odoo import http


# class SaleDateOrder(http.Controller):
#     @http.route('/sale_date_order/sale_date_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_date_order/sale_date_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_date_order.listing', {
#             'root': '/sale_date_order/sale_date_order',
#             'objects': http.request.env['sale_date_order.sale_date_order'].search([]),
#         })

#     @http.route('/sale_date_order/sale_date_order/objects/<model("sale_date_order.sale_date_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_date_order.object', {
#             'object': obj
#         })
