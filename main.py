from fcs_main import *

paises = cargar_datos(csv_ruta)

while True:
    menu()
    opcion = input_int('Ingrese una opción: ','¡Solo se permite números!')
    match opcion:
        case 1:
            paises = agregar_pais(paises)
            guardar_datos()
        case 2:
            pass
        case 3:
            buscar_pais(paises)
        case 4:
            pass
        case 5:
            ordenar_paises(paises)
        case 6:
            pass
        case 7:
            print('¡Saliendo del programa!')
            break