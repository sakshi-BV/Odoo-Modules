odoo.define('pos_demo.PosMobileButton', function (require) {
    'use strict';
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    // const ErrorPopup = require('point_of_sale.ErrorPopup');
    // const { useErrorHandlers, useAsyncLockedMethod } = require('point_of_sale.custom_hooks');

    const PosMobileButton = (ProductScreen) => class PosMobileButton extends ProductScreen {

        setup() {
            super.setup();
        }
        async onClick() {
            const allOrders = this.env.pos.get_order()
            console.log(allOrders)
            const { confirmed, payload: inputPhone } = await this.showPopup('PosMobileButtonPopup', {
                startingValue: allOrders.get_phone()
            });
            if (confirmed) {
                allOrders.set_phone(inputPhone);

            }

        }
        // @override For Enforce Customer Selection Before Order Proceeds:
        _onClickPay() {
            if (this.env.pos.get_order().partner == null) {
                this.showPopup('ErrorPopup', {
                    title: 'Customer Not Selected',
                    body: this.env._t('Please select the customer'),

                });
            }
            else {

                super._onClickPay()
            }

        }
    }
    PosMobileButton.template = 'PosMobileButton';
    Registries.Component.extend(ProductScreen, PosMobileButton);
    return PosMobileButton;
});
