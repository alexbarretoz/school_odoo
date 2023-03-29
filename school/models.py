from odoo import models, fields


class Subject(models.Model):
    
    _name= 'school.subject'
    
    name = fields.Char(string="Nombre")
    credits = fields.Integer(string='Credito')
    max_students = fields.Integer(string='max_estudiante')
    active = fields.Boolean(string='Activo')
    student_ids = fields.Many2many('body.function', 'organ_id', string='Función')
    teacher_id = fields.Many2one( 'body.function', 'organ_id', string='Función')


class Student(models.Model):

    _name= 'school.student'

    name = fields.Char(string="Nombre")
    birth_date= fields.Date(string='Fecha de Nacimiento')
    age = fields.Integer(string='Edad')
    final_exam_grade= fields.Float(string='Nota de examen final')
    subject_ids = fields.Many2many('body.function', 'organ_id', string='Función')


class Teacher(models.Model):
    _name= 'school.teacher'

    name = fields.Char(string="Nombre")
    profile= fields.Text(string='Perfil')
    subject_ids = fields.One2many('body.function', 'organ_id', string='Función')


