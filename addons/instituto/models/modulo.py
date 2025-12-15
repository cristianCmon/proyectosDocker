from odoo import fields, models

class Modulo(models.Model):
    # Nombre y descripción del modelo
    _name = 'instituto.modulo'
    _description = 'Módulo Formativo'

    nombre = fields.Char(string='Nombre del Módulo', required=True)
    horas = fields.Integer(string='Horas Lectivas')

    # Relación N:1 con Ciclo
    ciclo_id = fields.Many2one('instituto.ciclo', string='Ciclo Formativo', required=True, ondelete='restrict')

    # Relación N:1 con Profesor
    profesor_id = fields.Many2one('instituto.profesor', string='Profesor')

    # Relación N:M con Alumno
    alumno_ids = fields.Many2many('instituto.alumno', 'modulo_alumno_id', 'modulo_id', 'alumno_id', string='Alumnos Matriculados')
    