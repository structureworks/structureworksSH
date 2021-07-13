# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, modules, tools


class Message(models.Model):
    _inherit = 'mail.message'

    email_to = fields.Text('To', help='Message recipients (emails)')