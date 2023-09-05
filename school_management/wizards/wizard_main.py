from odoo import fields, models

class WizardDemo(models.TransientModel):
    _name = 'student.wizard'
    _description = 'demo wizard for student'

    remove_std = fields.Many2one('student.table', string = 'Student Name', required=True)


    def unlink(self):
        if self.remove_std:
            student_record= self.env['student.table'].search([('id', '=', self.remove_std.id)])
            student_record.unlink()

            return {
                'type' : 'ir.actions.client',
                'tag' : 'display_notification',
                'params' : {
                    'message' : ('Your record is deleted'),
                    'type' : 'success',
                    'next' : {
                        'type' : 'ir.actions.act_window_close'
                    } 
                }
            }

   