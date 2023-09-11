odoo.define('pos_demo.PosMobileButton', function (require) {
    'use strict';
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    // const ErrorPopup = require('point_of_sale.ErrorPopup');
    // const { useErrorHandlers, useAsyncLockedMethod } = require('point_of_sale.custom_hooks');

    const PosMobileButton = (ProductScreen) => class extends ProductScreen {

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
