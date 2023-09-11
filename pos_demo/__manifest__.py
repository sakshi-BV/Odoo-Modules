{
    'name': 'Pos Demo',
    'version': '16.0',
    'summary': 'demo module to practice point of sale',
    'description': 'demo module to practice point of sale',
    'author': 'Sakshi',
    'category': 'Apps',
    'license': 'LGPL-3',
    'depends':[ "point_of_sale","base"],
    'data': [
            'security/ir.model.access.csv',
            'views/PosOrderExtend.xml',
            'views/PartnerNote_view.xml',
    
    ],
    'assets':{
        'point_of_sale.assets': [
            'pos_demo/static/src/**/*',
        
        ],
    },
    'application': True,
    
}
