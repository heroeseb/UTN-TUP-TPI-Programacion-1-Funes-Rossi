from fcs_main import *

paises = cargar_datos(csv_ruta)

while True:
    opcion = seleccionar_menu()
    match opcion:
        case '1. Agregar un país.':
            paises = agregar_pais(paises)
            guardar_datos()
            continuar()
            limpiar_consola()
        case '2. Actualizar los datos de Población y Superficie de un País.':
            pass
        case '3. Buscar un país por nombre.':
            buscar_pais(paises)
            continuar()
            limpiar_consola()
        case '4. Filtrar países.':
            pass
        case '5. Ordenar países.':
            ordenar_paises(paises)
            continuar()
            limpiar_consola()
        case '6. Mostrar estadísticas.':
            pass
        case '7. Salir.':
            print('¡Saliendo del programa!')
            break