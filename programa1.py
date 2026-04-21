# Importamos herramientas para que Python pueda hablar con el sistema y con internet
import subprocess  # Sirve para ejecutar comandos de la terminal desde aquí
import requests    # Sirve para enviar mensajes a páginas web (en este caso, a Telegram)
import time        # Sirve para que el programa sepa esperar y no vaya demasiado rápido

# Aquí ponemos los nombres de "las cosas" para que sea fácil cambiarlos luego
# Ponemos el nombre del contenedor que queremos vigilar
CONTAINER_NAME = "telegram-whisper-bot" 
# Esta es la "llave" secreta que nos dio BotFather para nuestro bot
TELEGRAM_TOKEN = "8668529632:AAGLpsHMFpfwJfxtuVidygEP4qTri1ZcFjM"
# Este es tu ID personal de Telegram para que el bot sepa a quién escribirle a él
TELEGRAM_CHAT_ID = "1877485586"

# Esta función es como un interruptor: nos dice si el contenedor está encendido o no
def contenedor_activo():
    # Le pedimos a Docker que inspeccione el contenedor y nos diga si está "Running" (corriendo)
    resultado = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Running}}", CONTAINER_NAME],
        capture_output=True, # Captura lo que responde la terminal
        text=True            # Lo convierte en texto que podamos leer
    )
    # Si la respuesta es "true", significa que está encendido
    return resultado.stdout.strip() == "true"

# Esta función sirve para mandar el aviso a tu móvil
def enviar_mensaje(texto):
    # Esta es la dirección de internet de Telegram donde mandamos el mensaje
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # Aquí es donde realmente se envía el chat con tu ID y el texto que queramos
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": texto})

# Esto es un bucle infinito, el programa se queda funcionando siempre
while True:
    # Si la función de antes nos dice que el contenedor NO está activo...
    if not contenedor_activo():
        # ...entonces ejecutamos la función de enviar el mensaje de alerta
        enviar_mensaje(f"ALERTA: El contenedor {CONTAINER_NAME} está caído.")
    
    # Esperamos 60 segundos antes de volver a mirar, para no agobiar al ordenador
    time.sleep(60)