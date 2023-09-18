odoo.define('point_of_sale.LocationButtonComponent', function (require) {
    'use strict';

    // Importing required modules
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");

    class LocationButtonComponent extends PosComponent {

        // Setup method for initializing the component
        setup() {
            super.setup();

            // Using a click event listener
            useListener('click', this.onClick);

            // Getting the current order and a filtered list of locations based on configuration
            this.currentorder = this.env.pos.get_order();
            this.list = this.env.pos.locations.filter((loc)=> this.env.pos.config.location_res_config.includes(loc.id));
        }
        
        // Getter method to select a location
        get select_loc(){
            if (this.currentorder.setloc){
                return this.currentorder.setloc.id;
            }
            return false;
        }

        // Getter method for the selected location
        get selected_location(){
            let loc = this.currentorder.get_location();
            return loc ? loc.location_name : false;
        }

        // Handler for when the button is clicked
        async onClick() {
            console.log(this.env.pos);

            // Creating a selection list of locations
            const selectionList = this.list.map(loc => ({
                id: loc.id,
                label: loc.location_name,
                isSelected: loc.id == this.select_loc,
                item: loc,
            }));

            // Showing a popup for location selection
            const { confirmed, payload: selectedList } = await this.showPopup('SelectionPopup', {
                title : 'Select Location',
                list : selectionList
            });

            if(confirmed){
                this.currentorder.set_location(selectedList);
            }
        }
    }

    // Adding the control button to the Product Screen
    ProductScreen.addControlButton({
        component: LocationButtonComponent,
    });

    // Defining the template for the Location Button Component
    LocationButtonComponent.template = 'LocationButtonComponent';

    // Adding the Location Button Component to the Registries
    Registries.Component.add(LocationButtonComponent);

    return LocationButtonComponent;
});
