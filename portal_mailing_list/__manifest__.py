# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Mailing List Portal Subscribe/UnSubscribe',
    'version': '1.0',
    'category': 'Website',
    'summary': 'This is used for Subscribe and UnSubscribe to a Mailing Lists.',
    'description': """
This module is used to Subscribe and UnSubscribe to a Mailing Lists.
======================================
This module used to Subscribe and UnSubscribe to a Mailing Lists.
    """,
    'depends': ['portal', 'mass_mailing', 'website'],
    'data': [
        'views/mailing_list_portal_template.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
