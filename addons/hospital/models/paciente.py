from odoo import models, fields, api

class Paciente(models.Model):
    # Nombre y descripción del modelo
    _name = 'hospital.paciente'
    _description = 'Paciente del hospital'

    # Este atributo privado mostrará el nombre del socio en la relación con ejemplar.
    _rec_name = 'nombre_completo'

    # Propiedades
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    sintomatologia = fields.Text('Síntomas', required=True)
    # Para mostrar el nombre completo del paciente en la relación usaremos un campo calculado
    nombre_completo = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True, index=True)

    # RELACIÓN 1-N (para saber qué consultas tuvo este paciente)
    consulta_ids = fields.One2many('hospital.consulta', 'paciente_id', string='Historial de Consultas')


    # Campo calculado para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
