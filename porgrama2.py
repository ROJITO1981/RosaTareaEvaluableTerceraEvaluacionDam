# Importamos herramientas del sistema para manejar carpetas y mover archivos
import os      # Sirve para mirar qué hay en las carpetas y crear carpetas nuevas
import shutil  # Es la herramienta que usamos para "cortar y pegar" archivos

# Creamos una lista con los tipos de archivos que queremos ordenar
lista = ["png", "mp4", "doc"]

# PRIMERA PARTE: Crear las carpetas si no existen
for extension in lista:
    # Si NO existe una carpeta con el nombre de la extensión (ej: "png")...
    if not os.path.exists(extension):
        # ...entonces la creamos con este comando
        os.makedirs(extension)

# SEGUNDA PARTE: Revisar los archivos y moverlos
# Miramos todos los archivos que hay en la carpeta donde estamos ahora (".")
for archivo in os.listdir("."):
    # Nos aseguramos de que lo que estamos mirando es un archivo y no otra carpeta
    if os.path.isfile(archivo):
        # Rompemos el nombre del archivo por el punto (ej: "foto.png" -> ["foto", "png"])
        partes = archivo.split(".")
        
        # Si el archivo tiene extensión (es decir, si tiene más de una parte)
        if len(partes) > 1:
            # Cogemos la última parte, que siempre es la extensión (ej: "png")
            ext = partes[-1]
            
            # Si esa extensión está en nuestra lista de permitidos...
            if ext in lista:
                # ...movemos el archivo a su carpeta correspondiente
                # Es como decir: "mueve el archivo X a la carpeta X/archivo X"
                shutil.move(archivo, os.path.join(ext, archivo))

# Cuando termina todo el proceso, avisamos por pantalla
print("Archivos organizados.")