# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Cap Chatter Default Log Notes',
    'version': '1.0',
    'category': 'mail',
    'summary': 'Log notes is selected by default on any record And Download document direct many2one field of documents',
    'description': """
This module is used to Log notes is selected by default on any record.
This module also used to download a document on many2one field of documents in sale order.

======================================
This module used to Log notes is selected by default on any record. 
This module also used to download a document on many2one field of documents in sale order.
    """,
    'depends': ['mail', 'web'],
    'data': [
        'views/assets.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
