from odoo import fields, models

class PosLocationModel(models.Model):

    _name = 'pos.location.model'
    _description = 'having location for pos'
    _rec_name='location_name'

    location_name = fields.Char(string = 'Location')

