# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'CRM',
    'version': '1.8',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'website': 'https://www.odoo.com/app/crm',
    'depends': [
        'base',
    ],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',

        'data/crm_lead_merge_template.xml',
    ],
    # 'demo': [
    #     'data/crm_team_demo.xml',
    #     'data/mail_template_demo.xml',
    #     'data/crm_team_member_demo.xml',
    #     'data/mail_activity_type_demo.xml',
    #     'data/crm_lead_demo.xml',
    # ],
    'installable': True,
    'application': True,
    
    'license': 'LGPL-3',
}
