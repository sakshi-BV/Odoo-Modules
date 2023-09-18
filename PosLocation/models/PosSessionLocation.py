from odoo import fields, models, api

class PosSessionLocation(models.Model):
    """
    This class extends the 'pos.session' model to include functionality related to the 'pos.location.model'.
    """

    _inherit = 'pos.session'

    @api.model
    def _pos_ui_models_to_load(self):
        """
        Extends the '_pos_ui_models_to_load' method to include 'pos.location.model' in the list of models to be loaded.
        """
        model =  super()._pos_ui_models_to_load()
        model.append('pos.location.model')
        return model

    def _loader_params_pos_location_model(self):
        """
        Defines loader parameters for 'pos.location.model'.
        """
        return {
            'search_params': {
                'fields': ['location_name'],
            }
        }

    def _get_pos_ui_pos_location_model(self, params):
        """
        Retrieves data from 'pos.location.model' based on the provided parameters.
        """
        return self.env['pos.location.model'].search_read(**params['search_params'])

    def _loader_params_product_product(self):
        """
        Extends loader parameters for 'product.product' to include 'qty_available' field.
        """
        load_field = super()._loader_params_product_product()
        load_field.get('search_params').get('fields').append('qty_available')
        return load_field
