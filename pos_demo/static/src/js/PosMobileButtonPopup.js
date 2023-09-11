odoo.define('point_of_sale.PosMobileButtonPopup', function (require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { _lt } = require('@web/core/l10n/translation');
    const { useState } = owl;

    class PosMobileButtonPopup extends AbstractAwaitablePopup {
        /**
         * @param {Object} props
         * @param {string} props.startingValue
         */
        setup() {
            super.setup();
            this.state = useState({ phone: this.props.startingValue });

        }

        getPayload() {
            // console.log(this.state.phone,"thjg")
            return this.state.phone;
        }

        async confirm() {
            const customersWithSamePhone = await this.env.services.rpc({
                model: 'pos.order',
                method: 'search_count',
                args: [[['phone_number', '=', this.state.phone]]]
            });
            console.log(customersWithSamePhone)
            if (this.state.phone == null) {
                this.showPopup("ErrorPopup", { body: "Please enter the phone number" });
            }
            else if (customersWithSamePhone > 0) {
                this.showPopup("ErrorPopup", { body: "phone number already exist" })
            }

            else {
                super.confirm()
            }
        }
    }
    PosMobileButtonPopup.template = 'PosMobileButtonPopup';
    PosMobileButtonPopup.defaultProps = {
        confirmText: _lt('Ok'),
        cancelText: _lt('Cancel'),
        title: 'Phone Number',
        body: '',
    };

    Registries.Component.add(PosMobileButtonPopup);

});
