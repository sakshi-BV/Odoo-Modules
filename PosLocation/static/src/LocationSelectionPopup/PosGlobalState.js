odoo.define('PosLocation.PosGlobalLocation', function (require) {
    'use strict';

    const { PosGlobalState } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    
    const PosGlobalLocation = (PosGlobalState) => class extends PosGlobalState {


        async _processData(loadedData) {
            this.locations = loadedData['pos.location.model'];
            super._processData(loadedData)
        }

    }
    
    Registries.Model.extend(PosGlobalState,PosGlobalLocation);

});