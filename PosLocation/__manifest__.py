{
    'name': 'Pos Location',
    'version': '16.0',
    'summary': 'for practise pos many2one location field added',
    'description': 'for practise pos many2one location field added',
    'author': 'Sakshi',
    'category': 'Apps',
    'license': 'LGPL-3',
    'depends':[ "point_of_sale","pos_demo","base"],
    'data': [
            'security/ir.model.access.csv',
            'views/PosLocationView.xml',
            'views/PosOrderView.xml',
            'views/PosLocationSetting.xml',
    
    ],
    'assets':{
        'point_of_sale.assets': [
            'PosLocation/static/src/**/*',
        
        ],
    },
    'application': True,
    
}
