// Defining a custom Odoo component named 'PosMobileField'
odoo.define("point_of_sale.PosMobileField", function (require) {
    "use strict";

    const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit"); // Importing PartnerDetailsEdit module
    const Registries = require("point_of_sale.Registries"); // Importing Registries module

    // Defining PosMobileField as an extension of PartnerDetailsEdit
    const PosMobileField = (PartnerDetailsEdit)=> class PosMobileField extends PartnerDetailsEdit {

        // Setup function to initialize the component
        setup(){
            super.setup(); // Calling the setup function of the parent class
            this.changes.note = this.props.partner.note || ""; // Initializing 'note' with partner's note or an empty string
        }
    }

    PosMobileField.template = "PartnerDetailsEditTemplate"; // Setting the template for PosMobileField
    Registries.Component.extend(PartnerDetailsEdit, PosMobileField); // Extending PartnerDetailsEdit with PosMobileField
    return PosMobileField; // Exporting PosMobileField
});
