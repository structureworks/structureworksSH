# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rendering_sign = fields.Image('Rendering sign', help='Signature received through the portal.', copy=False, attachment=True,
                                  max_width=1024, max_height=1024)
    drawing_sign = fields.Image('Drawing sign', help='Signature received through the portal.', copy=False,
                                attachment=True,
                                max_width=1024, max_height=1024)


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
