from odoo import fields, models

class PosLocationSetting(models.TransientModel):

    _inherit = 'res.config.settings'

    location_config = fields.Many2many(related ='pos_config_id.location_res_config', readonly=False)


class PosConfigLocation(models.Model):

    _inherit = 'pos.config'

    location_res_config = fields.Many2many('pos.location.model')

