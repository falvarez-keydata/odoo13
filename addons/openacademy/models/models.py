# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Cursos"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
    def action_test(self):        
        #raise osv.except_osv(_("Warning!"), _(" Hello Mehdi Mokni !!."))
        raise ValidationError("Hola Mundo")
    
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    
    

class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"
    
    def action_test(self):        
        #raise osv.except_osv(_("Warning!"), _(" Hello Mehdi Mokni !!."))
        raise ValidationError("Hola Session")
    
    name = fields.Char(required=True)
    status_session = fields.Boolean(string="Status",default=False)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    #see_course = fields.Many2many('openacademy.course','name')
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain="[('instructor','=',True)]")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    
    # see_course = fields.Many2many(string="Nombres",comodel_name="openacademy.course",
    #     domain="[('name', '=', 'Daniel')]",
    # )
    

class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'openacademy.openacademy'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    

