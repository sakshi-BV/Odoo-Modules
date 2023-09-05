from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class Employee(models.Model):
    _name = 'employee.table'
    _description = 'Here we get the details of employees and store them in database'
    _rec_name = 'employee_name'
    # _inherit = 'teacher.table'

    employee_name = fields.Char(string='Employee Name', required=True)
    dob = fields.Date(string='D.O.B')
    age = fields.Integer(string='Age')
    gender = fields.Selection(string='Gender', selection=[(
        'male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    bio = fields.Text(string='Biography')
    countryz = fields.Many2one('res.country', string='Country')
    state = fields.Many2one(
        'res.country.state', string='States', domain="[('country_id','=',countryz)]")
    mobile_no = fields.Integer(string='Mobile No')
    _sql_constraints = [
        ('unique_number', 'unique (mobile_no)', 'Mobile number already exists!'), (
            'check_number', 'CHECK (LENGTH(mobile_no) = 10)', 'Incorrect mobile no formate!')
    ]
    employee_status = fields.Boolean(string='Active', default=True)
    hour_rate = fields.Float(string='Hour rates')
    hour = fields.Float(string='Working Hour')
    salary = fields.Float(string='salary', compute='_compute_salary')
    salary1 = fields.Float(string='salary1')
    counts = fields.Char('count', compute='_search_count', default='0')
    email = fields.Char('Email')
    department = fields.Char('Department')
    status = fields.Selection(
        [("draft", 'Draft'), ('confirmed', 'Confirmed')], default='draft')

    def action_confirm(self):
        self.status = 'confirmed'

    @api.model
    def create(self, vals):
        new_id = self.env['department.table']
        new_id.create({
            'department_name': vals['department']
        })

        record = super(Employee, self).create(vals)
        print(type(record),'aaaaaaaaa')
        return record

    def unlink(self):
        for employee in self:
            if not employee.employee_status:
                raise UserError("Cannot delete inactive employees.")

        record = super(Employee, self).unlink()
        print(type(record),'bbbbbbbbbbbbb')
        return record

    @api.constrains('age')
    def check_negative_age(self):
        for rec in self:
            if rec.age < 0:
                raise ValidationError("Age cannot be negative")

    @api.depends('hour_rate', 'hour')
    def _compute_salary(self):
        for rec in self:
            rec.salary = rec.hour_rate * rec.hour

    @api.onchange('hour_rate', 'hour')
    def _onchange_salary(self):
        for rec in self:
            rec.salary1 = rec.hour_rate * rec.hour

    @api.depends('gender')
    def _search_count(self):
        count = self.env['employee.table'].search_count(
            [('gender', '=', 'female')])
        self.counts = count

    def write(self, vals):
        for record in self:
            if 'gender' in vals and vals['gender'] == 'female':
                vals['email'] = 'femail.com'
            elif 'gender' in vals and vals['gender'] == 'male':
                vals['email'] = 'mail.com'
            else:
                vals['email'] = 'other.com'
        record = super(Employee, self).write(vals)
        print(type(record),'ccccccccccccccc')
