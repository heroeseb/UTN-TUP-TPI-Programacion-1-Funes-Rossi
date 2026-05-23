from fcs_main import *
import questionary
import csv
import os
csv_ruta = 'paises.csv'
paises = []
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

paises = cargar_datos(csv_ruta)
while True:
    limpiar_consola()
    opcion = seleccionar_menu()[0]
    match opcion:
        case "1":
            paises = agregar_producto(paises)
            continuar()
        case "2":
            actualizar_datos_pys(paises)
            continuar()
        case "3":
            buscar_pais(paises)
            continuar()
        case "4":
            filtrado_paises(paises) # arreglar sub-menu
        case "5":
            pass
        case "6":
            mostrar_estadisticas(paises)
            continuar()
        case "7":
            print("Hasta luego, ¡vuelva pronto!")
            guardar_datos(lista)
            break
        case _:
            print("lol")