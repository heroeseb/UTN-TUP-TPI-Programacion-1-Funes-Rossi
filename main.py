from fcs_main import *

paises = cargar_datos(csv_ruta)

input('Presione ¬Enter para comenzar')

while True:
    limpiar_consola()
    opcion = seleccionar_menu("Seleccione la acción a realizar:",['1. Agregar un país.','2. Actualizar los datos de Población y Superficie de un País.',
                '3. Buscar un país por nombre.','4. Filtrar países.',
                '5. Ordenar países.','6. Mostrar estadísticas.','7. Salir.'])[0]
    match opcion:
        case '1':
            try:
                nuevo_paises = agregar_pais(paises)
                if not nuevo_paises:
                    raise VariableVaciaError('No se actualizo la lista de paises')
                paises = nuevo_paises
            except VariableVaciaError as e:
                print(e)
            guardar_datos(paises)
            continuar()
        case '2':
            nuevo_paises = actualizar_datos_pys(paises)
            if nuevo_paises:
                paises = nuevo_paises
            guardar_datos(paises)
            continuar()
        case '3':
            buscar_pais(paises)
            continuar()
        case '4':
            filtrado_paises(paises)
            continuar()
        case '5':
            nuevo_paises = ordenar_paises(paises)
            if nuevo_paises:
                paises = nuevo_paises
            guardar_datos(paises)
            continuar()
        case '6':
            mostrar_estadisticas(paises)
            continuar()
        case '7':
            print('Hasta luego, ¡vuelva pronto!')
            break