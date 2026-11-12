import os
import math


'''
MENÚ PRINCIPAL¶
Listar contenido del directorio actual
Crear un nuevo directorio
Crear un archivo de texto
Escribir texto en un archivo existente
Eliminar un archivo o directorio
Mostrar información del archivo
Salir
'''
def listar_contenido():
    #Listar archivos y carpetas del directorio actual
    elementos = os.listdir()
    for elemento in elementos:
        #print(elemento)
        if os.path.isdir(elemento):
            print(f"Carpeta {elemento}")
        else:
            print(f"Archivo {elemento}")

def crear_directorio():
    nombre_carpeta = input("\nIntroduce el nombre de la carpeta nueva: ")
    try:
        os.mkdir(nombre_carpeta)
    except FileExistsError:
        print("Ya existe una carpeta con ese nombre")
    else:
        print(f"Se ha creado la carpeta {nombre_carpeta}")



while True:
    print(f"\nContenido de {os.getcwd()}")
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo")
    print("7. Salir\n")

    try:
        opcion = int(input("Escoge una tarea: "))
    except ValueError:
        print("\nIngresa una opción válida, un número entero\n")
        continue

    match opcion:
        case 1: 
            listar_contenido() # LLamada funcion
        case 2:
            crear_directorio()
        case 3:
            print("3")
        case 4:
            print("4")
        case 5:
            print("5")
        case 6:
            print("6")
        case 7: 
            print("Saliendo...")
            break
        case _ :
            print("\nIngresa un opción que esté dentro del menú\n")
        
            

    