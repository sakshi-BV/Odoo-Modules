from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta


class School(models.Model):
    _name = 'student.table'
    _description = 'Here we get the details of students'
    _rec_name = 'student_name'
    _inherit = ['mail.thread']

    student_name = fields.Char(
        string='Name', required=True, help='name of student', translate=False)
    standard = fields.Integer(string='Standard')
    class_teacher = fields.Many2one(
        'teacher.table', string='Class Teacher', compute='_compute_class_teacher', store=True)
    division = fields.Selection(
        [('A', 'A'), ('B', 'B')], string='Division')
    stream = fields.Selection(
        [("maths", "Maths"), ("commerce", "Commerce"), ("arts", "Arts")], string="Stream")
    roll_number = fields.Char(string='Roll Number',
                              default=lambda self: (('New')))
    enrollment_number = fields.Char(string='Enrollment_Number', readonly=1)
    street = fields.Char()
    street1 = fields.Char()
    city = fields.Char()
    state = fields.Many2one(
        'res.country.state', domain="[('country_id','=', countryz)]")
    countryz = fields.Many2one(
        'res.country')
    zip_code = fields.Char()

    phone_number = fields.Char(required=True, tracking=True)
    country_code = fields.Char(compute='_compute_country_code', store=False)
    dob = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age', compute='_compute_age',
                         store=True, inverse='_inverse_compute_age')
    description = fields.Text(string='Description')
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
    ], string='Birth Month', compute='_compute_birth_month', store=True)
    fee_status = fields.Selection(
        [('paid', 'PAID'), ('unpaid', 'UNPAID')], string='Fees Status', default='unpaid')
    teacher_list = fields.Many2one(
        'teacher.table', string='Teacher_list')

    parent_name = fields.Char(string='Parent Name')
    relation_with_student = fields.Selection(
        [('father', 'Father'), ('mother', 'Mother'), ('guardian', 'Guardian')], string='Relation with Student')
    parent_contact = fields.Char(string='Parent Contact')
    parent_email = fields.Char(string='Parent Email')
    aadhar_card = fields.Binary(string="Aadhar Card")

    previous_school_name = fields.Char(string='School Name')
    previous_enrollment_number = fields.Char(string='Enrollment Number')
    previous_admission_date = fields.Date(string='Admission Date')
    previous_leaving_date = fields.Date(string='Leaving Date')

    partner_id = fields.One2many('res.partner', 'company_id_mg')
    active = fields.Boolean(default=True)
    display = fields.Char(
        compute='_compute_display', string='Dispaly Name', default='wait')
    
    age_progress = fields.Integer(string='Progress', compute='_compute_form_progress')
    active_std = fields.Boolean(string='Active Student', default ='True')
    
    user_admin = fields.Many2one(
        'res.users', string="Admin", store=True)
    
   
    @api.constrains('phone_number')
    def check_phone_number(self):
        for rec in self:
            if len(rec.phone_number) != 10 or rec.phone_number.isdigit() == False:
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
            if rec.zip_code:
                if len(rec.zip_code) != 6 or rec.zip_code.isdigit() == False:
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

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.dob = today - relativedelta.relativedelta(years=rec.age)

    @api.depends('standard', 'division', 'stream')
    def _compute_class_teacher(self):
        for rec in self:
            if rec.standard <= 10:
                self.stream = False
                teacher = self.env['teacher.table'].search([
                    ('class_allotted', '=', rec.standard),
                    ('section_allotted', '=', rec.division),
                ], limit=1)

            elif rec.standard in [11, 12]:
                self.division = False
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

    @api.depends("countryz")
    def _compute_country_code(self):
        for rec in self:
            if rec.countryz:
                phone_number_code = rec.countryz.phone_code
                rec.country_code = "+" + str(phone_number_code)
            else:
                rec.country_code = False

    def open_url(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.google.com',
            'target': 'new',
        }

    def actiondone(self):
        for rec in self:
            rec.fee_status = "paid"

    def button_action(self):
        action = {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": 'teacher.table',

        }
        return action

    def wiz_action(self):
        # print(self._context)
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": 'student.wizard',
            "target": "new",
            
        }

    def default_get(self, fields_list):
        record = super(School, self).default_get(fields_list)
        record['previous_admission_date'] = fields.Date.today()
        return record

    @api.model
    def create(self, vals):
        if vals.get('roll_number', 'New') == 'New':
            vals['roll_number'] = self.env['ir.sequence'].next_by_code(
                'student.sequence')
        record = super(School, self).create(vals)
        record.enrollment_number = 'ENR-' + str(record.id).zfill(4)
        return record

    def _compute_display(self):
        for student in self:
            student.display = f"{student.student_name} ({student.standard})"
            

    @api.depends('age')
    def _compute_form_progress(self):
        for student in self:
            if student.age:
                student.age_progress = student.age
            else:
                student.age_progress = 0


    def student_email_action(self):
        print(self._context.get('button'),'================================')
        template_id = self.env.ref('school_management.email_template_edi_student').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send= True)

    def student_email_action1(self):
        recs = self.env['student.table'].search([])
        print(recs,"bbbbbbbbbbbbbbbbbbbbbbb")
        for rec in recs:
            template_id = rec.env.ref('school_management.email_template_edi_student').id
            rec.env['mail.template'].browse(template_id).send_mail(rec.id, force_send= True)

    def student_record_create_action(self):
        print('ousahbosuiadhsoiadjosiajop')
        for i in range(2):
            name = 'Student'+ str(i)
            age = 5+i
            phone_number = '123456789' + str(i)
            standard = '3'
            self.create({'student_name':name, 'age':age,'phone_number':phone_number,'standard':standard})
       

    def student_record_delete_action(self):
        recs = self.search([])
        for rec in recs:
            rec.unlink()

    def student_query_action(self):
        query ="insert into student_table(Student_name,standard,age,phone_number,active) values('New Record',10,15,1478523698,true)"
        self.env.cr.execute(query)
        self.env.cr.commit()
        

class Test(models.Model):

    _inherit = 'teacher.table'

    example = fields.Char(string='Example')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_id_mg = fields.Many2one('student.table')
