# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Openacademy(http.Controller):
    # @http.route('/contacto', auth='public', website=True)
    # def contacto_redirect(self):
    #     return request.redirect('/contactus')
    @http.route('/contacto', auth='public', website=True)
    def contacto_render(self):
        return "HEY"
    
    # def index(self, **kw):
    #     return "Hello, world"
    
    # @http.route('/openacademy/openacademy/', auth='public', website=True)
    # def index(self, **kw):
    #     return "Hello, world"

'''     @http.route('/openacademy/openacademy/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('openacademy.listing', {
            'root': '/openacademy/openacademy',
            'objects': http.request.env['openacademy.openacademy'].search([]),
        }) '''

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
