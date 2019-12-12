# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizardopenacademyreport(models.TransientModel):
    _name='openacademy.session'
    _description="Wizard para Session"
    
    title=fields.Char('Titulo',required=True)
    descripcion=fields.Text('Descripcion',required=True)
    date_init=fields.Date('Fecha')
    
    @api.multi
    def action_report(self):
        """Aqui va la logica del report print ('hola mundo')"""        
        return True