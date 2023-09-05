from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError

class Department(models.Model):
    _name = 'department.table'
    _description = 'Here we get the details of employees department'
    

    department_name = fields.Char(string='Department Name')
    