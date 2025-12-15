from odoo import models, fields, api

class Socio(models.Model):
    # Nombre y descripción del modelo
    _name = 'socio.biblioteca'
    _description = 'Socio de biblioteca'

    # Este atributo privado mostrará el nombre del socio en la relación con ejemplar.
    _rec_name = 'nombre_completo'

    # Propiedades
    nombre = fields.Char('Nombre de pila', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    id_socio = fields.Char('DNI', required=True, index=True)
    # Para mostrar el nombre completo de socio en la relación usaremos un campo calculado
    nombre_completo = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True, index=True)

    # RELACIÓN 1-N (Un socio puede tener muchos ejemplares prestados)
    ejemplar_ids = fields.One2many('ejemplar.prestamo', 'socio_id', string='Ejemplares Prestados')


    # Campo calculado para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
