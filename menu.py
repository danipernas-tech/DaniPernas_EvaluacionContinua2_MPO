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

while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o drectorio")
    print("6. Mostrar inormación del archivo")
    print("7. Salir\n")

    try:
        opcion = int(input("Escoge una tarea: "))
    except ValueError:
        print("\nIngresa una opción valida, un número entero\n")
        continue

    match opcion:
        case 1: 
            print("1") # LLamada funcion
        case 2:
            print("1")
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

        
            

    