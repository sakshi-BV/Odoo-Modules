from odoo import fields, models,api


class PosSessionLocation(models.Model):
    _inherit = 'pos.session'

    @api.model
    def _pos_ui_models_to_load(self):
        model =  super()._pos_ui_models_to_load()
        model.append('pos.location.model')
        return model
    

   
    def _loader_params_pos_location_model(self):
        return {
            'search_params': {
                'fields': ['location_name'],
            }
        }
    
    def _get_pos_ui_pos_location_model(self, params):
        return self.env['pos.location.model'].search_read(**params['search_params'])
    
#to add qty_available field value and diplay the quatity of product
    def _loader_params_product_product(self):
        load_field = super()._loader_params_product_product()
        load_field.get('search_params').get('fields').append('qty_available')
        return load_field
    