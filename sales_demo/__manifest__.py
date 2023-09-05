{
    'name': 'Sales Demo',
    'version': '16.0',
    'summary': 'test file',
    'sequence':1,
    'description': 'all the details are here',
    'author': 'Sakshi',
    'depends':['base','school_management'],
    'category': 'Apps',
    'license': 'LGPL-3',
    'data': [
       
            'security/ir.model.access.csv',
            'views/sales_demo_view.xml',
            'report/qweb_template.xml',
         
    ],
   
    'application': True
}