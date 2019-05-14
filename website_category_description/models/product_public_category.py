# -*- coding: utf-8 -*-


from odoo import models,fields




class ProductPublicCategory(models.Model):
    _inherit="product.public.category"
    
    
    description=fields.Html('Description')