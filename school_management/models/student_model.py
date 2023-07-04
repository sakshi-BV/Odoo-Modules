from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date


class School(models.Model):
    _name = 'student.table'
    _description = 'Here we get the details of students'
    _rec_name = 'student_name'
    _inherit = 'mail.thread'

    student_name = fields.Char(string='Name', required=True)
    standard = fields.Integer(string='Standard')
    class_teacher = fields.Many2one(
        'teacher.table', string='Class Teacher', compute='_compute_class_teacher')
    division = fields.Selection(
        [('a', 'A'), ('b', 'B')], string='Division')
    stream = fields.Selection(
        [("maths", "Maths"), ("commerce", "Commerce"), ("arts", "Arts")], string="Stream")
    roll_number = fields.Char(string='Roll Number')
    enrollment_number = fields.Char(string='Enrollment_Number', readonly=1)
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    state = fields.Many2one(
        'res.country.state', string='State', domain="[('country_id','=', countryz)]")
    countryz = fields.Many2one('res.country', string='Country')
    zip_code = fields.Char(string='Zip Code')
    phone_number = fields.Char(
        string='Phone number', required=True, tracking=True)
    dob = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    birth_month = fields.Selection([
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ], string='Birth Month', compute='_compute_birth_month', store=True, group="true")

    parent_name = fields.Char(string='Parent Name')
    relation_with_student = fields.Selection(
        [('father', 'Father'), ('mother', 'Mother'), ('guardian', 'Guardian')], string='Relation with Student')
    parent_contact = fields.Char(string='Parent Contact')
    parent_email = fields.Char(string='Parent Email')

    previous_school_name = fields.Char(string='School Name')
    previous_enrollment_number = fields.Char(string='Enrollment Number')
    previous_admission_date = fields.Date(string='Admission Date')
    previous_leaving_date = fields.Date(string='Leaving Date')

    @api.constrains('phone_number')
    def check_phone_number(self):
        for rec in self:
            if len(rec.phone_number) != 10:
                raise ValidationError("Invalid phone number")

            dual_record = self.search(
                [('phone_number', '=', rec.phone_number), ('id', '!=', rec.id)])
            if dual_record:
                raise ValidationError("Phone number should be unique")

    @api.constrains('standard')
    def check_standard(self):
        for rec in self:
            if (rec.standard < 1) or (rec.standard > 12):
                raise ValidationError("Their are only 1 to 12 standards")

    @api.constrains('zip_code')
    def check_zip_code(self):
        for rec in self:
            if len(rec.zip_code) != 6:
                raise ValidationError("Invalid zip code")
    
    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age < 4:
                raise ValidationError("Age should be greater than 3")
    
    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                dob = fields.Date.from_string(rec.dob)
                if dob.month < today.month or (dob.month == today.month and dob.day <= today.day):
                    rec.age = today.year - dob.year
                else:
                    rec.age = today.year - dob.year - 1
            else:
                rec.age = 0

    @api.depends('standard', 'division', 'stream')
    def _compute_class_teacher(self):
        for rec in self:
            if rec.standard <= 10:
                teacher = self.env['teacher.table'].search([
                    ('class_allotted', '=', rec.standard),
                    ('section_allotted', '=', rec.division),
                ], limit=1)
            elif rec.standard in [11, 12]:
                teacher = self.env['teacher.table'].search([
                    ('class_allotted', '=', rec.standard),
                    ('stream_allotted', '=', rec.stream)
                ], limit=1)
            else:
                teacher = False

            rec.class_teacher = teacher

    @api.depends('dob')
    def _compute_birth_month(self):
        for student in self:
            if student.dob:
                birth_month = fields.Date.from_string(
                    student.dob).strftime('%m')
                student.birth_month = birth_month

    @api.model
    def create(self, vals):
        record = super(School, self).create(vals)

        record.enrollment_number = 'ENR-' + str(record.id)

        return record

