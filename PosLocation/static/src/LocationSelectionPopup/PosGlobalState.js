odoo.define('PosLocation.PosGlobalLocation', function (require) {
    'use strict';

    // Importing required modules
    const { PosGlobalState } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    
    // Extending the PosGlobalState model
    const PosGlobalLocation = (PosGlobalState) => class extends PosGlobalState {

        // Override method for processing loaded data
        async _processData(loadedData) {
            // Extracting location data and assigning it to 'this.locations'
            this.locations = loadedData['pos.location.model'];
            super._processData(loadedData);  // Calling the parent method
        }

    }
    
    // Extending the PosGlobalState model with PosGlobalLocation
    Registries.Model.extend(PosGlobalState,PosGlobalLocation);
});
