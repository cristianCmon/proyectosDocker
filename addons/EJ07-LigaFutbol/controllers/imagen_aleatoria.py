# -*- coding: utf-8 -*-
from odoo import http # type: ignore
from odoo.http import request # type: ignore

import base64
from io import BytesIO

from PIL import Image # type: ignore
import random

class ImagenAleatoria(http.Controller):

    @http.route('/imagen/<int:ancho>/<int:alto>', auth='public', type='http')
    def crearImagen(self, ancho, alto):
        # CREAMOS IMAGEN VACÍA EN MODO RGB
        imagen = Image.new('RGB', (ancho, alto))
        pixeles = imagen.load()

        # CREAMOS BUCLES ANIDADOS PARA RECORRER CADA PÍXEL DE LA IMAGEN,
        # CREANDO UN COLOR DE FORMA ALEATORIA EN CADA ITERACIÓN
        for x in range(ancho):
            for y in range(alto):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                pixeles[x, y] = (r, g, b)

        # UTILIZAMOS BytesIO COMO BUFFER EN RAM
        buffer = BytesIO()
        
        # GUARDAMOS LA IMAGEN Pillow EN EL BUFFER COMO PNG
        imagen.save(buffer, format="PNG")

        # TRADUCIMOS EL CONTENIDO DEL BUFFER A base64
        imagenB64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # DEVOLVEMOS EL HTML MOSTRANDO LA IMAGEN RECIÉN CREADA
        return '''<div><h2>PÍXELES ALEATORIOS(%dx%d)</h2>
            <img src="data:image/png;base64,%s"/></div>''' % (ancho, alto, imagenB64)
