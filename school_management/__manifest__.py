{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Manage all students related informtion',
    'description': 'all the details of the students are here',
    'author': 'Sakshi',
    'depends':['base', 'mail'],
    'category': 'Apps',
    'data': [
            'security/ir.model.access.csv',
            "views/student_model_view.xml",
            "views/teacher_model_view.xml",
            "views/student_model_action.xml",
            "views/student_model_menu.xml",
            "data/demo_data.xml"
    ],
    'application': True
}