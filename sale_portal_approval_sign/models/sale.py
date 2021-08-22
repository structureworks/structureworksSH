# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('pre_confirmed', 'Pre Confirmed'), ('sale',)])
    rendering_sign = fields.Image('Rendering sign', help='Signature received through the portal.', copy=False, attachment=True,
                                  max_width=1024, max_height=1024)
    drawing_sign = fields.Image('Drawing sign', help='Signature received through the portal.', copy=False,
                                attachment=True,
                                max_width=1024, max_height=1024)

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        if not (self.product_id and self.product_uom and
                self.order_id.partner_id and self.order_id.pricelist_id and
                self.order_id.pricelist_id.discount_policy == 'without_discount' and
                self.env.user.has_group('product.group_discount_per_so_line')):
            return

#         self.discount = 0.0
        product = self.product_id.with_context(
            lang=self.order_id.partner_id.lang,
            partner=self.order_id.partner_id,
            quantity=self.product_uom_qty,
            date=self.order_id.date_order,
            pricelist=self.order_id.pricelist_id.id,
            uom=self.product_uom.id,
            fiscal_position=self.env.context.get('fiscal_position')
        )

        product_context = dict(self.env.context, partner_id=self.order_id.partner_id.id, date=self.order_id.date_order, uom=self.product_uom.id)

        price, rule_id = self.order_id.pricelist_id.with_context(product_context).get_product_price_rule(self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id)
        new_list_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id, self.product_uom_qty, self.product_uom, self.order_id.pricelist_id.id)

        if new_list_price != 0:
            if self.order_id.pricelist_id.currency_id != currency:
                # we need new_list_price in the same currency as price, which is in the SO's pricelist's currency
                new_list_price = currency._convert(
                    new_list_price, self.order_id.pricelist_id.currency_id,
                    self.order_id.company_id or self.env.company, self.order_id.date_order or fields.Date.today())
            discount = (new_list_price - price) / new_list_price * 100
            if (discount > 0 and new_list_price > 0) or (discount < 0 and new_list_price < 0):
                self.discount = discount
    
    
    @api.onchange('pricelist_id', 'order_line')
    def _onchange_pricelist_id(self):
        if self.order_line and self.pricelist_id and self._origin.pricelist_id != self.pricelist_id:
            self.show_update_pricelist = True
        else:
            self.show_update_pricelist = False


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self._context.get('from_sales_team'):
            teams = self.env['crm.team'].search([])
            args += [('id', 'in', teams.team_user_ids.mapped('user_id').ids)]
            return super(ResUsers, self).name_search(name, args, operator, limit)
        else:
            return super(ResUsers, self).name_search(name, args, operator, limit)


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self._context.get('sales_person'):
            member = self.env['team.user'].search([('user_id', '=', self._context.get('sales_person'))])
            args += [('team_user_ids', 'in', member.ids)]
            return super(CrmTeam, self).name_search(name, args, operator, limit)
        else:
            return super(CrmTeam, self).name_search(name, args, operator, limit)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def default_get(self, fields):
        res = super(ResPartner, self).default_get(fields)
        if res.get('type') == 'other':
            res['type'] = 'contact'
        teams = self.env['crm.team'].search([])
        if self._uid in teams.team_user_ids.mapped('user_id').ids:
            res['user_id'] = self._uid
        else:
            if res.get('parent_id'):
                parent = self.browse(res.get('parent_id'))
                res['user_id'] = parent.user_id.id
        return res
