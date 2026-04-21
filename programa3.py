# Importamos paquetes para leer archivos, manejar el sistema y usar textos raros
import sys
import csv
import os
import re

# Estas dos líneas son para poder crear las imágenes de los códigos de barras
from barcode import get
from barcode.writer import ImageWriter

# Esta función limpia el nombre de los archivos para que no tengan símbolos raros
def limpiar_nombre_archivo(nombre):
    nombre = nombre.strip() # Quita espacios al principio y al final
    # Cambia símbolos prohibidos (como / o :) por un guion bajo "_"
    nombre = re.sub(r'[\\/:*?"<>|]+', "_", nombre)
    # Cambia los espacios en blanco por guiones bajos
    nombre = re.sub(r"\s+", "_", nombre)
    return nombre

# Esta función prepara el número para que sea un código de barras válido
def id_a_ean13_base(id_texto):
    # Le quita comillas y espacios al número
    t = id_texto.strip().strip('"').strip("'")
    # Si no son todo números, nos da error
    if not t.isdigit():
        return None
    # El código EAN13 necesita máximo 12 números (el 13 lo pone él)
    if len(t) > 12:
        return None
    # Si es corto, le pone ceros a la izquierda hasta llegar a 12
    return t.zfill(12)

# Aquí empieza el programa principal
def main():
    # Miramos si al ejecutar el programa hemos puesto el nombre del archivo CSV
    if len(sys.argv) != 2:
        print("Uso: python3 programa3.py archivo.csv")
        return

    ruta_csv = sys.argv[1] # Guardamos el nombre del archivo que nos han dado

    # Comprobamos que el archivo CSV de verdad existe en la carpeta
    if not os.path.isfile(ruta_csv):
        print("No existe el archivo:", ruta_csv)
        return

    # Abrimos el archivo CSV para empezar a leer los nombres y los números
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        # El "lector" nos ayuda a separar las columnas por comas
        lector = csv.reader(f, delimiter=",", quotechar='"', skipinitialspace=True)

        # Vamos fila por fila del archivo
        for fila_num, fila in enumerate(lector, start=1):
            if not fila: # Si la línea está vacía, la saltamos
                continue

            # Necesitamos al menos dos cosas: el Nombre y el ID
            if len(fila) < 2:
                print(f"Linea {fila_num}: faltan columnas (nombre,ID)")
                continue

            # Guardamos el nombre y el ID quitando comillas
            nombre = fila[0].strip().strip('"').strip("'")
            id_leido = fila[1].strip().strip('"').strip("'")

            # Usamos las funciones de arriba para arreglar el nombre y el número
            nombre_archivo = limpiar_nombre_archivo(nombre)
            ean_base = id_a_ean13_base(id_leido)

            # Si el nombre está vacío, avisamos y saltamos
            if not nombre_archivo:
                print(f"Linea {fila_num}: nombre vacio, se salta")
                continue

            # Si el número no sirve para el código de barras, avisamos
            if ean_base is None:
                print(f"Linea {fila_num}: ID invalido (debe ser numero max 12 digitos)")
                continue

            # --- AQUÍ SE CREA EL DIBUJO DEL CÓDIGO DE BARRAS ---
            # Le decimos que use el formato "ean13" y que cree una imagen
            codigo = get("ean13", ean_base, writer=ImageWriter())
            # Lo guardamos con el nombre de la persona
            codigo.save(nombre_archivo)

    print("Listo.")

# Esto sirve para que el programa empiece a funcionar
if __name__ == "__main__":
    main()