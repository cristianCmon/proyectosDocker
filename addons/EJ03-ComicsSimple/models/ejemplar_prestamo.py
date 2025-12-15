from odoo import models, fields, api

class EjemplarPrestamo(models.Model):
    # Nombre y descripción del modelo
    _name = 'ejemplar.prestamo'
    _description = 'Ejemplar de cómic prestable'

    # Relación N:1 (muchos ejemplares para un cómic)
    comic_id = fields.Many2one('biblioteca.comic', string='Comic de Referencia', required=True, ondelete='cascade')
    # Relación N:1 (muchos ejemplares para un socio)
    socio_id = fields.Many2one('socio.biblioteca', string='Prestado a Socio')

    # Fechas de entrega y devolución
    fecha_inicio = fields.Date('Fecha de entrega')
    fecha_fin = fields.Date('Fecha de devolución')


    # Comprobación fecha de inicio
    @api.constrains('fecha_inicio')
    def _check_fecha_inicio(self):
        for record in self:
            if record.fecha_inicio and record.fecha_inicio > fields.Date.today():
                raise models.ValidationError('La fecha de entrega no puede ser posterior al día actual.')
            
    #Comprobación fecha de devolución
    @api.constrains('fecha_fin')
    def _check_fecha_fin(self):
        for record in self:
            if record.fecha_fin and record.fecha_fin < fields.Date.today():
                raise models.ValidationError('La fecha de devolución no puede ser anterior al día actual.')
