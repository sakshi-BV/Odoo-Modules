{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Manage all students related informtion',
    'description': 'all the details of the students are here',
    'author': 'Sakshi',
    'sequence': '0',
    'depends':['base', 'mail'],
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'maintainer':'Sakshi',
    'assets':{
        'web.assets_backend': [
            'school_management/static/src/component/**/*'
        ],
    },
    'data': [
            
            'security/ir.model.access.csv',
            "views/student_model_view.xml",
            "views/teacher_model_view.xml",
            "views/student_model_action.xml",
            "wizards/wizard_view.xml",
            "views/student_model_menu.xml",
            "views/component_assets.xml",
            "reports/controller_template.xml",
            'reports/student_details_template.xml',
            "data/mail_template.xml",
            "views/student_setting_view.xml",
            "data/sequence.xml",
            "data/cron.xml",
            
            
    ],
    'demo': [
        "data/demo_data.xml",
    ],
    'auto_install': False,
    'application': True,
    'active':False,
}