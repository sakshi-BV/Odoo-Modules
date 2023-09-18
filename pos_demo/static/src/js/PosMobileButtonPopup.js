// Defining a custom Odoo component named 'PosMobileButtonPopup'
odoo.define('point_of_sale.PosMobileButtonPopup', function (require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup'); // Importing AbstractAwaitablePopup module
    const Registries = require('point_of_sale.Registries'); // Importing Registries module
    const { _lt } = require('@web/core/l10n/translation'); // Importing translation utility
    const { useState } = owl; // Importing useState from Owl framework

    class PosMobileButtonPopup extends AbstractAwaitablePopup {

        /**
         * @param {Object} props
         * @param {string} props.startingValue
         */

        setup() {
            super.setup();
            this.state = useState({ phone: this.props.startingValue }); // Setting up state for phone with starting value from props
        }

        // Getting the payload (phone number)
        getPayload() {
            return this.state.phone;
        }

        // Confirming the input
        async confirm() {
            const customersWithSamePhone = await this.env.services.rpc({
                model: 'pos.order',
                method: 'search_count',
                args: [[['phone_number', '=', this.state.phone]]]
            });

            console.log(customersWithSamePhone);

            // Handling validation cases
            if (this.state.phone == null) {
                this.showPopup("ErrorPopup", { body: "Please enter the phone number" });
            }
            else if (customersWithSamePhone > 0) {
                this.showPopup("ErrorPopup", { body: "Phone number already exists" });
            }
            else {
                super.confirm();
            }
        }
    }

    PosMobileButtonPopup.template = 'PosMobileButtonPopup'; // Setting the template for PosMobileButtonPopup
    PosMobileButtonPopup.defaultProps = {
        confirmText: _lt('Ok'),
        cancelText: _lt('Cancel'),
        title: 'Phone Number',
        body: '',
    };

    Registries.Component.add(PosMobileButtonPopup); // Adding PosMobileButtonPopup to Registries
});
