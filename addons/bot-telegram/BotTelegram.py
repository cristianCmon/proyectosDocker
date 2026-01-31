import json
import requests # type: ignore
import os
from dotenv import load_dotenv # type: ignore
from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters # type: ignore

# BUSCA NUESTRO ARCHIVO .env Y CARGA SU CONTENIDO
load_dotenv()

# ASIGNAMOS VARIABLES DE ENTORNO A CONSTANTES
TOKEN = os.getenv('TOKEN_TELEGRAM')
API_SOCIOS = os.getenv('URL_API_ODOO_SOCIOS')


def peticionApiSocios(tipoPeticion, data=None, params=None):
    try:
        # ESTA VARIABLE ES NECESARIA DADA LA CONFIGURACIÓN DEL CONTROLADOR
        # YA QUE SÓLO ADMITE PETICIONES POR URL PARA MÉTODOS GET Y DELETE
        datosEnUrl = {'data': json.dumps(params)}

        if tipoPeticion == 'POST':
            respuesta = requests.post(API_SOCIOS, json=data)

        elif tipoPeticion == 'PUT':
            respuesta = requests.put(API_SOCIOS, json=data)

        elif tipoPeticion == 'GET':
            respuesta = requests.get(API_SOCIOS, params=datosEnUrl)

        elif tipoPeticion == 'DELETE':
            respuesta = requests.delete(API_SOCIOS, params=datosEnUrl)
        
        # IMPRIMIMOS POR CONSOLA EL RESULTADO PARA DEPURAR
        print(f"\n{tipoPeticion} Código {respuesta.status_code}: {respuesta.text}")
        # SI LA RESPUESTA ES CÓDIGO 200 DEVUELVE JSON PROCESADO, SINO DEVUELVE CÓDIGO DE ERROR
        return respuesta.json() if respuesta.status_code == 200 else f"Error {respuesta.status_code}"
    
    except Exception as e:
        return f"Error de conexión: {str(e)}"


async def manejadorBotTelegram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TEXTO QUE ESCRIBIMOS DESDE TELEGRAM
    mensajeTelegram = update.message.text
    
    try:
        if mensajeTelegram.startswith("Crear,"):
            partes = dict(item.split('=') for item in mensajeTelegram.replace("Crear,", "").replace('"', '').split(','))
            respuesta = peticionApiSocios('POST', data=partes)
            await update.message.reply_text(f"Nuevo socio registrado: {respuesta}")

        elif mensajeTelegram.startswith("Modificar,"):
            partes = dict(item.split('=') for item in mensajeTelegram.replace("Modificar,", "").replace('"', '').split(','))
            respuesta = peticionApiSocios('PUT', data=partes)
            await update.message.reply_text(f"Socio modificado: {respuesta}")

        elif mensajeTelegram.startswith("Consultar,"):
            num_socio = mensajeTelegram.split('=')[1].replace('"', '').strip()
            respuesta = peticionApiSocios('GET', params={'num_socio': num_socio})
            await update.message.reply_text(f"Datos del socio: {respuesta}")

        elif mensajeTelegram.startswith("Borrar,"):
            num_socio = mensajeTelegram.split('=')[1].replace('"', '').strip()
            respuesta = peticionApiSocios('DELETE', params={'num_socio': num_socio})
            await update.message.reply_text(f"Socio borrado: {respuesta}")

        else:
            ## MOSTRARÁ ESTE TEXTO SI EL MENSAJE ENVIADO NO EMPIEZA POR NINGUNA PALABRA CLAVE
            await update.message.reply_text("Orden NO soportada\nSólo se admite 'Crear', 'Modificar', 'Consultar' y 'Borrar'")

    # EVITA QUE EL BOT SE CUELGUE SI SE ENVÍA UN MENSAJE CON ALGÚN ERROR 'ORTOGRÁFICO'
    except Exception as e:
        await update.message.reply_text(f"Error al procesar comando: formato incorrecto.")


if __name__ == '__main__':
    # CONFIGURA Y CONSTRUYE APLICACIÓN CON NUESTRO TOKEN
    aplicacion = ApplicationBuilder().token(TOKEN).build()
    
    # FILTRO QUE REACCIONA A MENSAJES DE TEXTO QUE NO SEAN EL COMANDO /start
    manejadorMensaje = MessageHandler(filters.TEXT & (~filters.COMMAND), manejadorBotTelegram)
    aplicacion.add_handler(manejadorMensaje)
    
    print("\nBot de Telegram iniciado, en espera...")

    # MANTIENE EL BOT A LA ESCUCHA DE NUEVOS MENSAJES
    aplicacion.run_polling()
