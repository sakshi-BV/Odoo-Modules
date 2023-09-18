# Importing necessary modules from Odoo
from odoo import fields, models, api
from odoo.exceptions import ValidationError

# Inheriting 'res.partner' model to add a new field 'note'
class PosExtend(models.Model):
    _inherit ='res.partner'

    note = fields.Char()

    # Adding a constraint to validate the 'note' field
    @api.constrains('note')
    def note_validation(self):
        alldata = self.env['res.partner']
        for rec in self:
            count = alldata.search_count([['note','=',rec.note],['id','!=',rec.id]])
            if count > 0:
                raise ValidationError("Already Exist")

# Inheriting 'pos.session' model to extend the loader parameters for 'res.partner'
class PosSession(models.Model):
    _inherit = 'pos.session'

    # Extending loader parameters to include the 'note' field
    def _loader_params_res_partner(self):
        load_field = super(PosSession, self)._loader_params_res_partner()
        load_field.get('search_params').get('fields').append('note')
        return load_field
