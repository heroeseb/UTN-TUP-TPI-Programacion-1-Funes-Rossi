from fcs_main import *

paises = cargar_datos(csv_ruta)

while True:
    limpiar_consola()
    opcion = seleccionar_menu()
    match opcion:
        case '1. Agregar un país.':
            paises = agregar_pais(paises)
            guardar_datos()
            continuar()
        case '2. Actualizar los datos de Población y Superficie de un País.':
            actualizar_datos_pys(paises)
            continuar()
        case '3. Buscar un país por nombre.':
            buscar_pais(paises)
            continuar()
        case '4. Filtrar países.':
            filtrado_paises(paises) # arreglar sub-menu
        case '5. Ordenar países.':
            ordenar_paises(paises)
            continuar()
        case '6. Mostrar estadísticas.':
            mostrar_estadisticas(paises)
            continuar()
        case '7. Salir.':
            print('Hasta luego, ¡vuelva pronto!')
            break