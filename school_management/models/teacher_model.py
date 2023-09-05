from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Teacher(models.Model):
    _name = 'teacher.table'
    _description = 'Here we have class teachers name'
    _rec_name = 'teacher_name'

    teacher_name = fields.Char(string='Name', required=True)
    class_allotted = fields.Integer(string='Class', required=True)
    section_allotted = fields.Selection(
        selection=[('A', 'A'), ('B', 'B')], string='Section')
    stream_allotted = fields.Selection(selection=[(
        'maths', 'Maths'), ('commerce', 'Commerce'), ('arts', 'Arts')], string='Stream')
    
    test = fields.One2many('student.table', 'teacher_list', store=True)

    @api.constrains('class_allotted', 'section_allotted', 'stream_allotted')
    def check_unique_teacher(self):
        if self.class_allotted <= 10:
            all_teacher = self.env['teacher.table'].search(
                [('class_allotted', '=', self.class_allotted), ('section_allotted', '=', self.section_allotted), ('id', '!=', self.id)])

            if all_teacher:
                raise ValidationError("Already exist")

        elif self.class_allotted in [11, 12]:
            all_teacher = self.env['teacher.table'].search(
                [('class_allotted', '=', self.class_allotted), ('stream_allotted', '=', self.stream_allotted), ('id', '!=', self.id)])
            if all_teacher:
                raise ValidationError("Already exist")

        else:

            raise ValidationError("Enter Standard between 1 to 12")

    def name_get(self):
        teacher = []
        for record in self:
            if record.class_allotted <= 10:
                teacher_alot = str(record.teacher_name) + '  ' + \
                    str(record.class_allotted) + ' ' + \
                    str(record.section_allotted)
                teacher.append((record.id, teacher_alot))
            else:
                teacher_alot = record.teacher_name + '  ' + \
                    str(record.class_allotted) + ' ' + record.stream_allotted
                teacher.append((record.id, teacher_alot))
        return teacher

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):

        if args == None:
            args = []
        record = self.search(['|', '|', '|', ('teacher_name', operator, name), (
            'class_allotted', operator, name), ('section_allotted', operator, name), ('stream_allotted', operator, name)], limit=limit)

        return record.name_get()
    




