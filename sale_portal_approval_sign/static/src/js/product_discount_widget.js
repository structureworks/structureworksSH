odoo.define('sale_portal_approval_sign.product_discount', function (require) {
    "use strict";

    const ProductDiscount= require('sale.product_discount');
    const FieldsRegistry = require('web.field_registry');

    ProductDiscount.include({

        async reset(record, ev) {
//            if (ev && ev.data.changes && ev.data.changes.discount >= 0) {
//               this.trigger_up('open_discount_wizard');
//            }
//            this._super(...arguments);
        },
    });

});
