from odoo import http

class School_Controller(http.Controller):

    @http.route('/sakshi/sahu/', website = True, auth = 'public')
    def School(self, **kw):
        return http.request.render('school_management.controller_template_id',{'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],})
        

