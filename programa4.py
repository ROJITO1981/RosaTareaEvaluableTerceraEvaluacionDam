#para hablar con mi sistema operativo 
import os

# Funcion para procesar cada archivo y obtener el identificador
def obtener_id_alumno(archivo):
    # Separamos el nombre de la extension .png
    nombre_base = os.path.splitext(archivo)[0]
    
    # Extraemos los ultimos caracteres para usarlos como ID
    # Esto simula la extraccion del codigo de barras
    identificador = "ID-" + nombre_base[-3:]
    return identificador

def main():
    # Obtenemos la lista de todos los archivos en la carpeta actual
    lista_archivos = os.listdir(".")
    
    print("Escaneando archivos de la carpeta...")
    print("====================================")
    
    # Recorremos la lista con un bucle para buscar las imagenes
    for nombre_fichero in lista_archivos:
        
        # Filtramos para procesar solo los archivos que son imagenes PNG
        if nombre_fichero.lower().endswith(".png"):
            
            # Llamamos a la funcion para conseguir el ID
            codigo_detectado = obtener_id_alumno(nombre_fichero)
            
            # Limpiamos el nombre del archivo para mostrarlo por pantalla
            nombre_limpio = nombre_fichero.replace(".png", "")
            
            # Mostramos los resultados finales por consola
            print("Archivo procesado: " + nombre_fichero)
            print("Alumno: " + nombre_limpio)
            print("Codigo: " + codigo_detectado)
            print("------------------------------------")

# Punto de entrada para ejecutar el programa principal
if __name__ == "__main__":
    main()