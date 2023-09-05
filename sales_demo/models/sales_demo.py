from odoo import fields, models, api


class AbsDemo(models.AbstractModel):

    _name = 'abstract.model'
    _description ='practice abstraction model'
    _abstract = True

    abs_name = fields.Char(string = 'abstract_field1')
    abs_class = fields.Char(string = 'abstract_field2')


class Demo(models.Model):
    
    _name = 'sales.demo'
    _description = 'here we practiced some features od sales modeule'
    _rec_name ='name'
    _inherit = "abstract.model"


    name = fields.Char(string='Order Reference', required=True)
    date_order = fields.Date(string='Order Date')
    amount_total = fields.Float(string='Total Amount')
    partner_id = fields.Many2one('res.partner', string='Customer')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')],
                             string='Status', default='draft')
    student_image = fields.Binary(string ='Image')
    student= fields.Many2many('student.table','many_demo','main_id','ref_id',string='student name')
   

    val1= fields.Float()
    val2 = fields.Float()
    result = fields.Integer(compute = '_compute_result')    

    # @api.depends('val1', 'val2','name')
    # @api.onchange('val1', 'val2',"name")
    def _compute_result(self):
        for  rec in self:
            rec.result = (rec.val1 + rec.val2)



    

 


    
