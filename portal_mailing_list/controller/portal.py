# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import binascii

from odoo import fields, http, _
from odoo.http import request
from odoo.tools.translate import _
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError


class CustomerPortal(CustomerPortal):

    @http.route(['/my/mailing_list/'], type='http', auth="public", website=True, methods=['GET', 'POST'])
    def portal_my_mailing_list(self, access_token=None):
        access_token = access_token or request.httprequest.args.get('access_token')
        mailing_contact = request.env['mailing.contact'].sudo().search([('access_token', '=', access_token)], limit=1)
        vals = {'mailing_contact': mailing_contact}
        return request.render("portal_mailing_list.portal_mailing_list_template", vals)

    @http.route(['/update/mailing_list'], type='http', auth="public", website=True, methods=['GET', 'POST'])
    def portal_update_mailing_list(self, **kwargs):
        print("\n\n222222222----->", kwargs)
        mailing_contact = request.env['mailing.contact'].sudo().search([('id', '=', kwargs.get('record_id'))])
        keys = [int(key) for key, val in kwargs.items() if val == 'on']
        for line in mailing_contact.subscription_list_ids:
            if line.id in keys:
                line.write({'opt_out': True})
            else:
                line.write({'opt_out': False})
        return request.render("portal_mailing_list.mailing_list_unsubscribe_submitted", {})
