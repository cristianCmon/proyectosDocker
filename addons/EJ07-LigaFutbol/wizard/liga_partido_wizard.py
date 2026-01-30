# -*- coding: utf-8 -*-
from odoo import models, fields # type: ignore

class LigaPartidoWizard(models.TransientModel):
    _name = 'liga.partido.wizard'
    _description = 'Wizard para registrar un partido'

    # CAMPOS DEL MODELO QUE USAREMOS EN EL WIZARD
    equipo_casa = fields.Many2one('liga.equipo', string='Equipo Local', required=True)
    equipo_fuera = fields.Many2one('liga.equipo', string='Equipo Visitante', required=True)
    goles_casa = fields.Integer('Goles Local', default=0)
    goles_fuera = fields.Integer('Goles Visitante', default=0)
    jornada = fields.Integer('Jornada', default=1, required=False)

    def crear_partido(self):
        # REFERENCIA DEL MODELO DESTINO
        modeloLigaPartido = self.env['liga.partido']
        # RECORREMOS tODO EL MODELO
        for wiz in self:
            # POR CADA ELEMENTO SE CREARÁ UN REGISTRO (SÓLO 1 EN ESTE CASO)
            modeloLigaPartido.create({
                'equipo_casa': wiz.equipo_casa.id,
                'equipo_fuera': wiz.equipo_fuera.id,
                'goles_casa': wiz.goles_casa,
                'goles_fuera': wiz.goles_fuera,
                'jornada': wiz.jornada
            })
        
        # CIERRA EL WIZARD Y REFRESCA LA VISTA ACTUAL
        return {'type': 'ir.actions.client', 'tag': 'reload'}
