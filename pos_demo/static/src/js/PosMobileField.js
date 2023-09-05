odoo.define("point_of_sale.PosMobileField", function (require) {
    "use strict";

    const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit");
    const Registries = require("point_of_sale.Registries");

    const PosMobileField = (PartnerDetailsEdit)=> class PosMobileField extends PartnerDetailsEdit {
        setup(){
            super.setup()
            this.changes.note = this.props.partner.note || ""
        }

    }
    PosMobileField.template = "PartnerDetailsEditTemplate";

    Registries.Component.extend(PartnerDetailsEdit, PosMobileField);

    return PosMobileField;
});