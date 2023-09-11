odoo.define('point_of_sale.PosLocationOrder', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const { Order } = require('point_of_sale.models');

    const PosLocationOrder = (Order) => class PosLocationOrder extends Order {
        
        //@override
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.location_name = this.setloc
            return json;
        }
        //@override
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.set_location(json.location_name)
        }
        

        set_location(location) {
            this.setloc = location
        }


        get_location() {
            return this.setloc
        }

        //@override
        // export_for_printing() {
        //     const result = super.export_for_printing(...arguments);
        //     if (this.get_phone()) {
        //         result.phone_number = this.get_phone();
        //     }
        //     console.log(result, 'bbbbbbbbbbbb')
        //     return result;
        // }
    };

    Registries.Model.extend(Order, PosLocationOrder);
    return PosLocationOrder
});