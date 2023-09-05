/*@odoo-module*/
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class HelloWorld extends Component {
   static template = "HelloWorld"
}

registry.category("actions").add("action_component", HelloWorld);