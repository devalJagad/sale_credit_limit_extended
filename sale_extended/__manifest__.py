# -*- coding: utf-8 -*-
{
    'name': 'Custom Credit Limit Extension',
    'version': '1.0',
    'depends': ['sale', 'account'],
    'category': 'Sales',
    'summary': 'Enhances credit limit checks for sales orders',
    'author': "Deval Jagad",
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
}
