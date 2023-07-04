from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Teacher(models.Model):
    _name = 'teacher.table'
    _description = 'Here we have class teachers name'
    _rec_name = 'teacher_name'

    teacher_name = fields.Char(string='Name', required=True)
    class_allotted = fields.Integer(string='Class', required=True)
    section_allotted = fields.Selection(selection = [('a', 'A'), ('b', 'B')], string='Section')
    stream_allotted = fields.Selection(selection = [('maths', 'Maths'), ('commerce', 'Commerce'), ('arts', 'Arts')],string='Stream')

    @api.constrains('class_allotted','section_allotted','stream_allotted')
    def check_unique_teacher(self):
        if self.class_allotted <= 10:
            all_teacher = self.env['teacher.table'].search(
                [('class_allotted', '=', self.class_allotted), ('section_allotted', '=', self.section_allotted),('id', '!=' , self.id)])
        
            if all_teacher:
                raise ValidationError("Already exist")
            
        elif self.class_allotted in [11, 12]:
            all_teacher = self.env['teacher.table'].search(
                [('class_allotted', '=', self.class_allotted), ('stream_allotted', '=', self.stream_allotted),('id', '!=' , self.id)])
            if all_teacher:
                raise ValidationError("Already exist")
            
        else:

                raise ValidationError("Enter Standard between 1 to 12")
            
    
