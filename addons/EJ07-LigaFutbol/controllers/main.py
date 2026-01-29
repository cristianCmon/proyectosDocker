# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result
    
    
    # NUESTRO WEB CONTROLLER PARA ELIMINAR EMPATES
    # http://localhost:9001/eliminarempates
    @http.route('/eliminarempates', type='http', auth='none')
    def eliminarPartidosConEmpate(self):
        # OBTENEMOS TODOS LOS REGISTROS DE LA TABLA DE LA BD
        partidos = request.env['liga.partido'].sudo().search([])

        # LISTA TEMPORAL EN LA QUE GUARDAREMOS EMPATES EXISTENTES
        listaEmpates = []

        # RECORREMOS TODOS LOS REGISTROS
        for partido in partidos:
            # COMPROBAMOS SI HAY EMPATES Y LOS AÑADIMOS A LA LISTA
            if partido.goles_casa == partido.goles_fuera:
                listaEmpates.append(partido)

        # VARIABLE TEMPORAL DE TOTAL EMPATES, NECESARIA PORQUE DESPUÉS DEL BORRADO len(listaEmpates) SIEMPRE SERÁ 0
        empatesTotales = len(listaEmpates)

        # SI HAY EMPATES ELIMINAMOS LOS REGISTROS Y MOSTRAMOS LA RESPUESTA SOLICITADA
        if empatesTotales > 0:
            for empate in listaEmpates:
                empate.unlink()

            respuesta = "El total de empates eliminados ha sido de: " + str(empatesTotales)
        # SI NO HAY EMPATES LO INDICAREMOS TAMBIÉN
        else:
            respuesta = "NO se han podido realizar el borrado porque NO se han detectado empates"

        # DEVOLVEMOS LA RESPUESTA ESPECIFICANDO QUE ES TEXTO PLANO PARA EVITAR POSIBLES ERRORES
        return request.make_response(respuesta, [('Content-Type', 'text/plain')])
