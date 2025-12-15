from odoo import models, fields

class Consulta(models.Model):
    # Nombre y descripción del modelo
    _name = 'hospital.consulta'
    _description = 'Registro de consultas realizadas'

    # Propiedades
    fecha_atencion = fields.Datetime(string='Fecha y Hora', default=fields.Datetime.now, required=True)
    diagnostico = fields.Text(string='Diagnóstico')

    # Relaciones N:1
    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True)
    medico_id = fields.Many2one('hospital.medico', string='Médico', required=True)
