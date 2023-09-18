// Defining a custom Odoo component named 'ButtonComponentAdd'
odoo.define('point_of_sale.ButtonComponentAdd', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent'); // Importing PosComponent module
    const ProductScreen = require('point_of_sale.ProductScreen'); // Importing ProductScreen module
    const Registries = require('point_of_sale.Registries'); // Importing Registries module
    const { useListener } = require("@web/core/utils/hooks"); // Importing useListener utility

    class ButtonComponentAdd extends PosComponent {

        setup() {
            super.setup();
            useListener('click', this.onClick);    // Setting up a listener for the pre-defined 'click' event 
            useListener('ondelete', this.onDelete);    // Setting up a listener for a custom 'delete' event (must be triggered elsewhere to define it)
        }

        // Handling the 'click' event
        async onClick() {
            const allOrders = this.env.pos.get_order(); // Getting the current order
            console.log(allOrders); // Logging the current order
            const { confirmed, payload: inputPhone } = await this.showPopup('PosMobileButtonPopup', {
                startingValue: allOrders.get_phone() // Displaying a popup for inputting a phone number, pre-populated with the current order's phone
            });

            if (confirmed) {
                allOrders.set_phone(inputPhone); // Setting the inputted phone number to the current order if confirmed
            }
        }

        // Handling a custom 'delete' event
        async onDelete() {
            const allOrders = this.env.pos.get_order(); // Getting the current order
            allOrders.remove_orderline(allOrders.get_selected_orderline()); // Removing the selected order line
        }
    }

    // Adding ButtonComponentAdd to the ProductScreen control buttons
    ProductScreen.addControlButton({
        component: ButtonComponentAdd,
    });

    ButtonComponentAdd.template = 'ButtonComponentAdd'; // Setting the template for ButtonComponentAdd
    Registries.Component.add(ButtonComponentAdd); // Adding ButtonComponentAdd to Registries
    return ButtonComponentAdd; // Exporting ButtonComponentAdd
});
