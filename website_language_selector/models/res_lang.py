# -*- coding: utf-8 -*- 


from odoo import models,fields




class ResLang(models.Model):
    _inherit='res.lang'
    
    
    flag_image = fields.Binary('Flag')