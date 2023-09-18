from odoo import fields, models

class PosLocationModel(models.Model):
    """
    This class defines the Odoo model 'pos.location.model' which is used for managing locations in the Point of Sale system.
    """

    _name = 'pos.location.model'
    _description = 'having location for pos'
    _rec_name = 'location_name'

    location_name = fields.Char(string='Location')
    """
    This field represents the name of the location. It is of type Char (string) and will be displayed in the user interface.
    """
