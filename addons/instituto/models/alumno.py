from odoo import fields, models, api

class Alumno(models.Model):
    # Nombre y descripción del modelo
    _name = 'instituto.alumno'
    _description = 'Alumno de instituto'

    # Este atributo privado mostrará el nombre del socio en la relación con ejemplar.
    _rec_name = 'nombre_completo'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)

    # Relación N:M con Módulos
    modulo_ids = fields.Many2many(
        'instituto.modulo', 'modulo_alumno_id', 'alumno_id', 'modulo_id', string='Módulos Matriculados')

    # Campo calculado para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
            