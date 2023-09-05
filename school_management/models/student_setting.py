from odoo import fields, models


class StudentSetting(models.TransientModel):

    _inherit = ['res.config.settings']

    cancel_days = fields.Integer(string='Cancel Days', config_parameter="school_management.cancel_days")
