# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import uuid


class MailingContact(models.Model):
    _inherit = 'mailing.contact'

    access_token = fields.Char(required=True, default=lambda x: uuid.uuid4().hex, index=False, copy=False)

    def action_set_access_token(self):
        self.access_token = uuid.uuid4().hex