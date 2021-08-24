# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Portal Rendering/Drawing Approval',
    'version': '1.0',
    'category': 'Website',
    'summary': 'This is used for Approval for a Rendering/Drawing Approval.',
    'description': """
This module is used to Approval for a Rendering/Drawing Approval.
======================================
This module used to Approval for a Rendering/Drawing Approval.
    """,
    'depends': ['portal', 'sale', 'website_sale'],
    'data': [
        'data/ir_model_fields.xml',
        'views/sale_order_view.xml',
        'views/sale_portal_template.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
