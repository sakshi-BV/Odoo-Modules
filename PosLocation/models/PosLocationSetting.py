from odoo import fields, models

class PosLocationSetting(models.TransientModel):
    """
    This class extends the 'res.config.settings' model and adds a Many2many field called 'location_config' to store
    configurations related to POS locations.
    """

    _inherit = 'res.config.settings'

    location_config = fields.Many2many(related='pos_config_id.location_res_config', readonly=False)
    """
    This field establishes a Many-to-Many relationship with the 'pos.location.model'. It is related to the field 
    'location_res_config' in the 'pos.config' model and is not read-only.
    """

class PosConfigLocation(models.Model):
    """
    This class extends the 'pos.config' model to add a Many2many field called 'location_res_config' for associating 
    specific POS configurations with locations.
    """

    _inherit = 'pos.config'

    location_res_config = fields.Many2many('pos.location.model')
    """
    This field allows the association of specific POS configurations with locations. It establishes a Many-to-Many 
    relationship with the 'pos.location.model'.
    """
