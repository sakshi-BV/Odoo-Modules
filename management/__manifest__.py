{
    'name': 'Management',
    'version': '16.0',
    'summary': 'manage the employe details',
    'description': 'all the details of the employee are here',
    'author': 'Sakshi',
    'category': 'Apps',
    'license': 'LGPL-3',
    'depends':["base","mail"],
    'data': [
            'security/ir.model.access.csv',
            'views/office_management_view.xml',
            'views/department_view.xml',
            'views/office_management_action.xml',
            'views/office_management_menu.xml'
    ],
    'application': True
}
