// Defining a custom Odoo component named 'PosMobileButton'
odoo.define('pos_demo.PosMobileButton', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen'); // Importing ProductScreen module
    const Registries = require('point_of_sale.Registries'); // Importing Registries module

    // Defining PosMobileButton as an extension of ProductScreen
    const PosMobileButton = (ProductScreen) => class extends ProductScreen {

        // @override For Enforce Customer Selection Before Order Proceeds:
        _onClickPay() {
            // Checking if a customer is selected before proceeding with the order
            if (this.env.pos.get_order().partner == null) {
                this.showPopup('ErrorPopup', {
                    title: 'Customer Not Selected',
                    body: this.env._t('Please select the customer'),
                });
            }
            else {
                super._onClickPay(); // Proceeding with the payment if a customer is selected
            }
        }
    }

    PosMobileButton.template = 'PosMobileButton'; // Setting the template for PosMobileButton
    Registries.Component.extend(ProductScreen, PosMobileButton); // Extending ProductScreen with PosMobileButton
    return PosMobileButton; // Exporting PosMobileButton
});
