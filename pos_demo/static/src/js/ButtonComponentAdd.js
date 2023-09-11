odoo.define('point_of_sale.ButtonComponentAdd', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");

    class ButtonComponentAdd extends PosComponent {

        setup() {
            super.setup();
            useListener('click', this.onClick);    //pre define event 'click' 
            useListener('ondelete', this.onDelete);    //userdefine event 'delete' you have to trigger it to define it
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

        async onDelete() {
            const allOrders = this.env.pos.get_order()
            allOrders.remove_orderline(allOrders.get_selected_orderline());

            // const allOrders_line = this.env.pos.get_order().orderlines

            // console.log(allOrders, 'aaaaaaaaaaaaa');
            
            // for (const orderLine of allOrders_line) {
            //     allOrders.remove_orderline(orderLine);

            // }
        }
    }
    ProductScreen.addControlButton({
        component: ButtonComponentAdd,
    });
    ButtonComponentAdd.template = 'ButtonComponentAdd';
    Registries.Component.add(ButtonComponentAdd);
    return ButtonComponentAdd;

});