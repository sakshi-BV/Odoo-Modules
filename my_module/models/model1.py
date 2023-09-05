from odoo import fields, models


class MyModel(models.Model):
    _name = 'data.table'
    _description = 'My Module Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_discription = fields.Date(string ='date') 
    expected_price = fields.Float(string ='Expected price', required=True)
    selling_price = fields.Float(string ='Selling price', required=True)
    garden = fields.Boolean(string='Garden', required=True)
    garage = fields.Boolean(string='Garage', required=True)
    seller_name = fields.Char(string='seller_name', required=True)
    seller_address = fields.Char(string='seller_address', required=True)
