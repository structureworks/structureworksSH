odoo.define('portal_mailing_list.MailListUnsubscribe', function (require) {
'use strict';
    var publicWidget = require('web.public.widget');

    publicWidget.registry.MailListUnsubscribe = publicWidget.Widget.extend({
        selector: '#mail_list_forms',
        events: {
            'click .select_all_list': '_onClickSelectAll',
            'click .unselect_all_list': '_onClickUnSelectAll',
        },

        _onClickSelectAll: function (ev) {
            this.$el.find('input[type="checkbox"]').each(function() {
                if (this.checked == false){
                    this.click('checked', true)
                }
            });
        },

        _onClickUnSelectAll: function (ev){
            this.$el.find('input[type="checkbox"]').each(function() {
                if (this.checked == true){
                    this.click('checked', false)
                }
            });
        },

    });
});
