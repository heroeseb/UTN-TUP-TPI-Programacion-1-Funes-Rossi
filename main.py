from fcs_main import *
import questionary
#     print('Iniciamos lista y cargamos datos')
#     paises = cargar_datos(csv_ruta)
#     print(paises)
#     print('Punto 1')
#     paises = agregar_producto(paises)
#     print('Guardo países en el csv')
#     guardar_datos(paises)
#     print(paises)
#     print('Punto 3, buscar países')
#     buscar_pais(paises)

while True:
    limpiar_consola()
    opcion = seleccionar_menu()[0]
    match opcion:
        case "1":
            agregar_producto(lista)
        case "2":
            actualizar_datos_pys(paises)
        case "3":
            buscar_pais(lista)
        case "4":
            filtrado_paises(paises)
        case "5":
            pass
        case "6":
            mostrar_estadisticas(paises)
            continuar()
        case "7":
            print("Hasta luego, ¡vuelva pronto!")
            break
        case _:
            print("lol")