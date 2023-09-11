odoo.define('point_of_sale.PosPhoneOrder', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const { Order } = require('point_of_sale.models');

    const PhoneNumber = (Order) => class PhoneNumber extends Order {
        
        //@override
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.phone_number = this.phone_no
            return json;
        }
        //@override
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.set_phone(json.phone_number)
        }

        set_phone(mobile) {
            this.phone_no = mobile
        }

        get_phone() {
            return this.phone_no
        }
        //@override
        export_for_printing() {
            const result = super.export_for_printing(...arguments);
            if (this.get_phone()) {
                result.phone_number = this.get_phone();
            }
            console.log(result, 'bbbbbbbbbbbb')
            return result;
        }
    };

    Registries.Model.extend(Order, PhoneNumber);
    return PhoneNumber
});