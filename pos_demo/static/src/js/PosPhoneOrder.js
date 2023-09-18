// Defining a custom Odoo component named 'PosPhoneOrder'
odoo.define('point_of_sale.PosPhoneOrder', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries'); // Importing Registries module
    const { Order } = require('point_of_sale.models'); // Importing Order class from point_of_sale.models

    // Defining PhoneNumber as an extension of Order
    const PhoneNumber = (Order) => class PhoneNumber extends Order {
        
        // Override export_as_JSON function to include phone number in the exported JSON
        //@override
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.phone_number = this.phone_no;
            return json;
        }

        // Override init_from_JSON function to set the phone number when initializing from JSON
        //@override
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.set_phone(json.phone_number);
        }

        // Function to set the phone number
        set_phone(mobile) {
            this.phone_no = mobile;
        }

        // Function to get the phone number
        get_phone() {
            return this.phone_no;
        }

        // Override export_for_printing function to include phone number in the printed data
        //@override
        export_for_printing() {
            const result = super.export_for_printing(...arguments);
            if (this.get_phone()) {
                result.phone_number = this.get_phone();
            }
            console.log(result, 'bbbbbbbbbbbb');
            return result;
        }
    };

    Registries.Model.extend(Order, PhoneNumber); // Extending Order with PhoneNumber
    return PhoneNumber; // Exporting PhoneNumber
});
