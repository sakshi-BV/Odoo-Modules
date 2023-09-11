odoo.define('point_of_sale.LocationButtonComponent', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");

    class LocationButtonComponent extends PosComponent {

        setup() {
            super.setup();
            useListener('click', this.onClick);  
            this.currentorder = this.env.pos.get_order()
            this.list = this.env.pos.locations.filter((loc)=> this.env.pos.config.location_res_config.includes(loc.id));
        }
        
        get select_loc(){
            if (this.currentorder.setloc){
                return this.currentorder.setloc.id
            }
            return false
        }

        get selected_location(){
            let loc = this.currentorder.get_location()
            return loc ? loc.location_name : false
        }


        async onClick() {
            console.log(this.env.pos)
            const selectionList = this.list.map(loc => ({
                id: loc.id,
                label: loc.location_name,
                isSelected:loc.id == this.select_loc,
                item: loc,
            }));
            const {confirmed, payload : selectedList}= await this.showPopup('SelectionPopup',{
                title : 'Select Location',
                list : selectionList
            });
            if(confirmed){
                this.currentorder.set_location(selectedList)
            }
            
        }

    }
    ProductScreen.addControlButton({
        component: LocationButtonComponent,
    });
    LocationButtonComponent.template = 'LocationButtonComponent';
    Registries.Component.add(LocationButtonComponent);
    return LocationButtonComponent;

});