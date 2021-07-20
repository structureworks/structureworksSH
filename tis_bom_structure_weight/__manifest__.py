# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

{
    'name': 'BOM Structure Weight & Volume',
    'version': '14.0.0.0',
    'category': 'Manufacturing/Manufacturing',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'sequence': 1,
    'website': 'http://www.technaureus.com/',
    'depends': ['mrp'],
    'price': 20,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': 'Weight and Volume in BOM Structure Report',
    'description': """
    This module includes weight and volume of products in bom structure report
    """,
    'data': [
        'report/mrp_report_bom_structure.xml'
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
