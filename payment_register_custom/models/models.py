# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaymentPopUp(models.Model):
    _inherit = 'account.payment.register'
    journal_id = fields.Many2one(
        comodel_name='account.journal',
        compute='', store=True, readonly=False, precompute=True,
        check_company=True,
        domain="[('type', 'in', ['cash','bank']),('company_id', '=', company_id)]")
    nuevo_campo = fields.Char(string="Skeree",default='Hola')
    
# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100