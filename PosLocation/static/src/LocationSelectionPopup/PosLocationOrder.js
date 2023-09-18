odoo.define('point_of_sale.PosLocationOrder', function (require) {
    'use strict';

    // Importing required modules
    const Registries = require('point_of_sale.Registries');
    const { Order } = require('point_of_sale.models');

    // Extending the Order model with location-related functionality
    const PosLocationOrder = (Order) => class PosLocationOrder extends Order {
        
        //@override
        export_as_JSON() {
            // Call the parent method and add location information to the JSON data
            const json = super.export_as_JSON(...arguments);
            json.location_name = this.setloc;
            return json;
        }

        //@override
        init_from_JSON(json) {
            // Call the parent method and set the location from JSON data
            super.init_from_JSON(...arguments);
            this.set_location(json.location_name);
        }

        set_location(location) {
            // Method to set the location
            this.setloc = location;
        }

        get_location() {
            // Method to get the location
            return this.setloc;
        }

        // Uncommented code for exporting data for printing
        // export_for_printing() {
        //     const result = super.export_for_printing(...arguments);
        //     if (this.get_phone()) {
        //         result.phone_number = this.get_phone();
        //     }
        //     console.log(result, 'bbbbbbbbbbbb')
        //     return result;
        // }
    };

    // Extending the Order model with PosLocationOrder
    Registries.Model.extend(Order, PosLocationOrder);
    return PosLocationOrder;
});
