from odoo import fields, models, api

class Profesor(models.Model):
    # Nombre y descripción del modelo
    _name = 'instituto.profesor'
    _description = 'Profesor de instituto'

    # Este atributo privado mostrará el nombre del socio en la relación con ejemplar.
    _rec_name = 'nombre_completo'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)

    # Relación 1:N con Módulos
    modulo_ids = fields.One2many('instituto.modulo', 'profesor_id', string='Módulos Impartidos')

    # Campo calculado para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
