from odoo import models, fields


#TABLA DE SUBJECTS
class Subject(models.Model):
    
    _name= 'school.subject'
    
    name = fields.Char(string="Nombre")
    credits = fields.Integer(string='Credito')
    max_students = fields.Integer(string='max_estudiante')
    active = fields.Boolean(string='Activo')
    student_ids = fields.Many2many('school.student', string='id_estudiante')
    teacher_ids = fields.Many2one( 'school.teacher',string='id_profesor')

#TABLA DE STUDENT
class Student(models.Model):

    _name= 'school.student'

    name = fields.Char(string="Nombre")
    birth_date= fields.Date(string='Fecha de Nacimiento')
    age = fields.Integer(string='Edad')
    final_exam_grade= fields.Float(string='Nota de examen final')
    subject_ids = fields.Many2many('school.subject', string='id_materias')

#TABLA DE PROFESOR
class Teacher(models.Model):
    _name= 'school.teacher'

    name = fields.Char(string="Nombre")
    profile= fields.Text(string='Perfil')
    subject_ids = fields.One2many('school.subject','teacher_ids', readonly=False)



