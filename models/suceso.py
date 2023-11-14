from odoo import fields

name = fields.Char(required=True, size=20, string="Suceso")
descripcion = fields.Text(string="A Descripción do Suceso")  # string é a etiqueta do campo
nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')