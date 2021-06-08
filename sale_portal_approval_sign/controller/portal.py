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

    @http.route(['/my/orders/<int:order_id>/approve_sign_rendering'], type='json', auth="public", website=True)
    def portal_approve_sign_rendering(self, order_id, access_token=None, name=None, signature=None, send_label=None):

        # get from query string if not on json param
        access_token = access_token or request.httprequest.args.get('access_token')
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order.')}

        if not signature:
            return {'error': _('Signature is missing.')}

        try:
            order_sudo.write({
                'rendering_sign': signature,
            })
            request.env.cr.commit()
        except (TypeError, binascii.Error) as e:
            return {'error': _('Invalid signature data.')}

        return {
            'force_refresh': True,
            'redirect_url': order_sudo.get_portal_url(),
        }

    @http.route(['/my/orders/<int:order_id>/approve_sign_drawing'], type='json', auth="public", website=True)
    def portal_approve_sign_drawing(self, order_id, access_token=None, name=None, signature=None, send_label=None):

        # get from query string if not on json param
        access_token = access_token or request.httprequest.args.get('access_token')
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order.')}

        if not signature:
            return {'error': _('Signature is missing.')}

        try:
            order_sudo.write({
                'drawing_sign': signature,
            })
            request.env.cr.commit()
        except (TypeError, binascii.Error) as e:
            return {'error': _('Invalid signature data.')}

        return {
            'force_refresh': True,
            'redirect_url': order_sudo.get_portal_url(),
        }

    @http.route(['/write_partner_industry/'], type='http', methods=['POST'], auth="public", csrf=False)
    def write_partner_industry(self, partner_id, industry_id, **kw):
        if partner_id:
            partner = request.env['res.partner'].sudo().browse(int(partner_id))
            partner.sudo().write({'industry_id': industry_id})
        return False
