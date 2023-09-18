# Importing necessary modules from Odoo
from odoo import fields, models, api

# Inheriting 'pos.order' model to add a new field 'phone_number'
class PosExtend(models.Model):
    _inherit ='pos.order'

    phone_number = fields.Char()

    # Overriding the '_order_fields' method to include 'phone_number' in the order fields
    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosExtend, self)._order_fields(ui_order)
        order_fields['phone_number'] = ui_order.get('phone_number')
        return order_fields
