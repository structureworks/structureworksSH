odoo.define('cap_chatter_default_log_note/static/src/components/chatter_topbar/chatter_topbar.js', function (require) {
'use strict';

const ChatterTopbar = require('mail/static/src/components/chatter_topbar/chatter_topbar.js');

const { patch } = require('web.utils');

patch(ChatterTopbar, 'cap_chatter_default_log_note/static/src/components/chatter_topbar/chatter_topbar.js',
    {
        mounted () {
            this.chatter.showLogNote();
        },

});

});
