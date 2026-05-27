from fcs_main import *

paises = cargar_datos(csv_ruta)

while True:
    limpiar_consola()
    opcion = seleccionar_menu()[0]
    match opcion:
        case '1':
            paises = agregar_pais(paises)
            guardar_datos(paises)
            continuar()
        case '2':
            paises = actualizar_datos_pys(paises)
            guardar_datos(paises)
            continuar()
        case '3':
            buscar_pais(paises)
            continuar()
        case '4':
            filtrado_paises(paises)
            continuar()
        case '5':
            paises = ordenar_paises(paises)
            guardar_datos(paises)
            continuar()
        case '6':
            mostrar_estadisticas(paises)
            continuar()
        case '7':
            print('Hasta luego, ¡vuelva pronto!')
            break