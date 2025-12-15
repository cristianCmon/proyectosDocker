from odoo import fields, models

class Ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'Ciclo Formativo'

    nombre = fields.Char(string='Nombre del Ciclo', required=True)
    codigo = fields.Char(string='Código', required=True, copy=False)

    # Relación 1:N con Módulos
    modulo_ids = fields.One2many('instituto.modulo','ciclo_id', string='Módulos del Ciclo')
    