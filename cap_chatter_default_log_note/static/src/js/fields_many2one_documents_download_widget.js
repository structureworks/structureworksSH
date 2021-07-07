odoo.define('cap_chatter_default_log_note.fields_many2one_documents_download_widget', function (require) {
"use strict";

var relationalFields = require('web.relational_fields');
var core = require('web.core');
var session = require('web.session');

var _t = core._t;

/**
 * Override of FieldMany2One to add a button Download for downloading the document
 */

var FieldMany2One = relationalFields.FieldMany2One;
FieldMany2One.include({

    /**
     * Add a button to Download a Document
     *
     * @override
     * @private
     */
    _renderReadonly: function () {
        var def = this._super.apply(this, arguments);
        if (this.field.relation == "documents.document" && this.value && this.model == "sale.order") {
            var $downloadButton = $('<a>', {
                title: _t('Download Document'),
                href: _.str.sprintf('/documents/content/%s', this.value.res_id),
                class: 'ml-3 d-inline-flex align-items-center',
            });
            $downloadButton.prepend($('<i>', {class: 'fa fa-download'}));
            this.$el = this.$el.add($downloadButton);
        }

        return def;
    },
});

return FieldMany2One;

});
