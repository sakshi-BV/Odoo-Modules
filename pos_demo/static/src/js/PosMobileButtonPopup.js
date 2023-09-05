odoo.define('point_of_sale.PosMobileButtonPopup', function (require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { _lt } = require('@web/core/l10n/translation');
    const { Order } = require('point_of_sale.models');
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

    const PhoneNumber = (Order) => class PhoneNumber extends Order {
        constructor(obj, options) {
            super(...arguments);
        }
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
            console.log(result,'bbbbbbbbbbbb')
            return result;
        }
    };

    Registries.Model.extend(Order, PhoneNumber);
    return PhoneNumber
});


    // return PosMobileButtonPopup;


