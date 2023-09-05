from odoo import fields, models, api
    
class PosExtend(models.Model):
    _inherit ='pos.order'

    phone_number =fields.Char()

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosExtend, self)._order_fields(ui_order)
        order_fields['phone_number'] = ui_order.get('phone_number')
        return order_fields
    












