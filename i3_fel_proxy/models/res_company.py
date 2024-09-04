# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"
    
    usuario_proxy = fields.Char(string='Usuario Proxy')
    clave_proxy = fields.Char(string='Clave Proxy')
    token_firma_fel = fields.Char(string='Proxy Token')
    token_por_factura = fields.Boolean(string='Token por factura', default=1)        
    es_pruebas_fel = fields.Boolean(string='Ambiente de pruebas', default=0)        
    frases_fel = fields.Char(string='Frases FEL', default=1)
    escenario_fel = fields.Integer('Frase Escenario FEL', default=1)
    