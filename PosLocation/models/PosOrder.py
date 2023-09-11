from odoo import fields, models, api
    
class PosExtend(models.Model):
    _inherit ='pos.order'

    location = fields.Many2one('pos.location.model',string = 'Location', readonly=True)

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosExtend, self)._order_fields(ui_order)
        order_fields['location'] = ui_order.get('location_name').get('id')
        return order_fields
    