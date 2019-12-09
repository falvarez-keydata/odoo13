# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_date_order(models.Model):
#     _name = 'sale_date_order.sale_date_order'
#     _description = 'sale_date_order.sale_date_order'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
