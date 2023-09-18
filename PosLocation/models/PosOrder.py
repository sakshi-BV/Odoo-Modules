from odoo import fields, models, api

class PosExtend(models.Model):
    _inherit ='pos.order'

    # Adding a Many-to-One relationship field to associate each order with a location.
    location = fields.Many2one('pos.location.model', string='Location', readonly=True)

    @api.model
    def _order_fields(self, ui_order):
        """
        Overrides the '_order_fields' method to include the 'location' field in the order fields.
        """
        order_fields = super(PosExtend, self)._order_fields(ui_order)

        # Get the location ID from the UI order and add it to the order fields
        order_fields['location'] = ui_order.get('location_name').get('id')

        return order_fields
