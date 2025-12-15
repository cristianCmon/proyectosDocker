from odoo import models, fields, api

class Medico(models.Model):
    # Nombre y descripción del modelo
    _name = 'hospital.medico'
    _description = 'Médico del hospital'

    # Este atributo privado mostrará el nombre del socio en la relación con ejemplar.
    _rec_name = 'nombre_completo'

    # Propiedades
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    numero_colegiado = fields.Char("Nº colegiado", required=True)
    # Para mostrar el nombre completo del paciente en la relación usaremos un campo calculado
    nombre_completo = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True, index=True)

    # RELACIÓN 1-N (Un médico puede haber atendido a muchos pacientes)
    consulta_ids = fields.One2many('hospital.consulta', 'medico_id', string='Consultas Atendidas')


    # Campo calculado para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
