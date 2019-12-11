# -*- coding: utf-8 -*-
# from odoo import http


# class Widget-slider(http.Controller):
#     @http.route('/widget-slider/widget-slider/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/widget-slider/widget-slider/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('widget-slider.listing', {
#             'root': '/widget-slider/widget-slider',
#             'objects': http.request.env['widget-slider.widget-slider'].search([]),
#         })

#     @http.route('/widget-slider/widget-slider/objects/<model("widget-slider.widget-slider"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('widget-slider.object', {
#             'object': obj
#         })
