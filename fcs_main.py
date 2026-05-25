import csv
import os
import questionary
csv_ruta = 'paises.csv'
paises = []

# Función para cargar datos
def cargar_datos(ruta):
    paises = []
    try:
        with open(ruta, 'r', encoding='utf-8', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    fila['nombre'] = fila['nombre']
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    fila['continente'] = fila['continente']
                    paises.append(fila)
                except (ValueError, KeyError, TypeError):
                    print('Se ignoró una línea inválida del CSV.')
    except FileNotFoundError:
        print('El archivo no existe. Se creará una lista vacía.')
    except PermissionError:
        print('Error... No tenés permiso de lectura en este archivo.')
    return paises

# Función para guardar datos
Fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']

def guardar_datos(lista):
    try:
        with open(csv_ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=Fieldnames)
            writer.writeheader()
            writer.writerows(lista)
            print('Se guardaron correctamente los datos.')
    except PermissionError:
        print('¡Error! No se pudo guardar. El archivo está abierto por otro programa o no hay permisos.')

# Validación de inputs
def input_str(mensaje, mensaje_2=None):
    while True:
        try:
            input_salid = input(mensaje).strip()
            if not input_salid.replace(' ', '').isalpha():
                raise TypeError
            return input_salid
        except TypeError:
            print(mensaje_2 if mensaje_2 else 'Error de tipo')

def input_int(mensaje, mensaje_2=None):
    while True:
        try:
            input_salid = int(input(mensaje))
            return input_salid
        except ValueError:
            print(mensaje_2 if mensaje_2 else 'Error de valor')

# Limpiar consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para continuar
def continuar():
    input("Presione ¬Enter para continuar")

# funcion para quitar tildes
def quitar_tildes(texto):
    texto = texto.lower()
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
        'ñ': 'n'
    }
    for letra_tilde, letra_normal in reemplazos.items():
        texto = texto.replace(letra_tilde, letra_normal)
    return texto


# Seleccionar con questionary
def seleccionar_menu():
    opcion = questionary.select(
        message="Seleccione la acción a realizar:",
        choices=['1. Agregar un país.','2. Actualizar los datos de Población y Superficie de un País.',
                '3. Buscar un país por nombre.','4. Filtrar países.',
                '5. Ordenar países.','6. Mostrar estadísticas.','7. Salir.']
    ).ask()
    return opcion

# Punto 1
def agregar_pais(lista):
    continentes = {'africa':'África','america':'América','antartida':'Antártida','asia':'Asia','europa':'Europa','oceania':'Oceanía'}
    nombre = input_str('Ingrese el nombre del país: ', '¡Ingrese un nombre válido')
    poblacion = input_int('Ingrese la cantidad de población: ', '¡Ingrese una cantidad válida!')
    while not poblacion > 0:
        print('¡El número debe ser mayor a cero!')
        poblacion = input_int('Ingrese la cantidad de población: ', '¡Ingrese una cantidad válida!')
    superficie = input_int('Ingrese la superficie del país: ', '¡Ingrese un número válido!')
    while not superficie > 0:
        print('¡La superficie debe ser mayor a cero!')
        superficie = input_int('Ingrese la superficie del país: ', '¡Ingrese un número válido!')
    continente = input_str('Ingrese el continente al que pertenece el país: ', 'Ingrese un continente válido.')
    while not(quitar_tildes(continente) in continentes.keys()):
        print('Por favor ingrese un continente válido.')
        continente = input_str('Ingrese el continente al que pertenece el país: ', 'Ingrese un continente válido.')
    if not (nombre and poblacion and superficie and continente):
        print('¡Faltan datos o se cargaron incorrectamente los datos...!')
    else:
        diccionario = {
            'nombre': nombre.capitalize(),
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continentes[quitar_tildes(continente)]
        }
        lista.append(diccionario)
        print('¡Se agregó correctamente el país!')
    return lista

# punto 2
def actualizar_datos_pys(paises):
    encontrado = False
    pais_actu = input_str("¿Cual país desea actualizar?: ","Inserte un nombre que se encuentre en la lista.").capitalize()
    for d in paises:
        if pais_actu == d["nombre"]:
            encontrado = True  
            nv_poblacion = input_int(f"¿Cual sera la nueva poblacion para {pais_actu}?: ","Inserte un valor valido.")
            while not nv_poblacion > 0:
                print("La cantidad de poblacion debe ser un valor numerico mayor a cero.")
                nv_poblacion = input_int(f"¿Cual sera la nueva poblacion para {pais_actu}?: ","Inserte un valor valido.")
            nv_superficie = input_int(f"¿Cual sera la nueva superficie para {pais_actu}?: ", "Inserte un valor valido.")
            while not nv_superficie > 0:
                print("La cantidad de superficie debe ser un valor numerico mayor a cero.")
                nv_superficie = input_int(f"¿Cual sera la nueva superficie para {pais_actu}?: ", "Inserte un valor valido.")
            d["poblacion"] = nv_poblacion 
            d["superficie"] = nv_superficie
            print("País actualizado correctamente.")
    if not encontrado: print("No se encontro un país...")

# Punto 3
def buscar_pais(lista):
    '''Buscar un país por nombre (coincidencia parcial o exacta).'''
    encontro_coincidencia = False
    nombre = input_str('Ingrese el nombre del país que desea buscar: ', 'Ingrese un nombre válido.').capitalize()
    for i in range(len(lista)):
        nombre_lista = lista[i]['nombre']
        if quitar_tildes(nombre) in quitar_tildes(nombre_lista):
            if quitar_tildes(nombre[0]) == quitar_tildes(nombre_lista[0]):
                encontro_coincidencia = True
                print(f"Nombre del país: {lista[i]['nombre']} | Población: {lista[i]['poblacion']} | Superficie: {lista[i]['superficie']} | Continente: {lista[i]['continente']}")
    if not encontro_coincidencia:
        print('No se encontraron coincidencias.')

# punto 4
def filtrado_paises(paises):
    while True:
        print("""Eliga el filtro:
1) Continente;
2) Rango de población;
3) Rango de superficie;
4) Volver atras.""")
        opcion = input_int("","Ingrese un valor numerico valido")
        match opcion:
            case 1:
                encontrado = False
                while True:
                    filtro = input_str("Ingrese el continente: ","Trate de ingresar el nombre correctamente.").capitalize()
                    for d in paises:
                        if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.")
                        elif filtro == "America":
                            filtro = "América"
                            if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.")
                        elif filtro == "Africa":
                            filtro = "África"
                            if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.")
                        elif filtro == "Oceania":
                            filtro = "Oceanía"
                            if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.") 
                    if not encontrado: print("No hay ningun país con ese continente.")
                    break
            case 2:
                encontrado = False
                while True:
                    filtro = input_int("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.")
                    while not filtro > 0:
                        print("La cantidad debe ser mayor a cero. Minimo 1.")
                        filtro = input_int("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.")
                    filtro2 = input_int("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.")
                    for d in paises:
                        if filtro <= d["poblacion"] and d["poblacion"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.")
                    if not encontrado: print("No hay ningun país que coincida con ese rango de población.")
                    break
            case 3:
                encontrado = False
                while True:
                    filtro = input_int("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.")
                    while not filtro > 0:
                        print("La cantidad debe ser mayor a cero. Minimo 1.")
                        filtro = input_int("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.")
                    filtro2 = input_int("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.")
                    for d in paises:
                        if filtro <= d["superficie"] and d["superficie"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.")
                    if not encontrado: print("No hay ningun país que coincida con ese rango de superficie.")
                    break
            case 4:
                print("Volviendo...")
                break
            case _:
                print("Eliga una opción presentada en pantalla.")

# Punto 5
def ordenar_paises(lista):
    print('Ordenar países por:')
    print('1. Nombre')
    print('2. Población')
    print('3. Superficie')
    opcion = input('Ingrese una opción: ').strip()
    opcion = quitar_tildes(opcion)
    match opcion:
        case '1' | 'nombre':
            lista.sort(key= lambda x:x['nombre'])
        case '2' | 'poblacion':
            lista.sort(key= lambda x:x['poblacion'])
        case '3' | 'superficie':
            print('1. Ascendente')
            print('2. Descendente')
            opcion3 = input('Ingrese una opción: ').strip().lower()
            match opcion3:
                case '1' | 'ascendente':
                    lista.sort(key= lambda x:x['superficie'])
                case '2' | 'descendente':
                    lista.sort(key= lambda x:x['superficie'],reverse=True)
                case _:
                    print('¡Por favor ingrese una opción correcta!')
        case _:
            print('¡Por favor ingrese una opción correcta!')
    return lista

# punto 6
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return
    lista_poblaciones = list(map(lambda x: x["poblacion"], paises))
    lista_superficie = list(map(lambda x: x["superficie"], paises))
    mayor = max(lista_poblaciones)
    menor = min(lista_poblaciones)
    for d in paises:
        if mayor == d["poblacion"]: pais_ma = d["nombre"]
        if menor == d["poblacion"]: pais_me = d["nombre"]
    print(f"""El país con mayor población es: {pais_ma}, con una cantidad de: {mayor} habitantes.
El país con mayor población es: {pais_me}, con una cantidad de: {menor} habitantes.""")
    print(f"El promedio de población es: {sum(lista_poblaciones) / len(lista_poblaciones)}.")
    print(f"El promedio de superficie es: {sum(lista_superficie) / len(lista_superficie)}.")
    americanos = 0
    europeos = 0
    africanos = 0
    asiaticos = 0
    oceanicos = 0
    for d in paises:
        if d["continente"] == "América": americanos += 1
        elif d["continente"] == "África": africanos += 1
        elif d["continente"] == "Europa": europeos += 1
        elif d["continente"] == "Asia": asiaticos += 1
        elif d["continente"] == "Oceanía": oceanicos += 1
    print(f"""Cantidad de paises en..:
América: {americanos};
Europa: {europeos};
Asia: {asiaticos};
África: {africanos};
Oceanía: {oceanicos}.""")


if __name__ == '__main__':
    print('Iniciamos lista y cargamos datos')
    paises = cargar_datos(csv_ruta)
    print(paises)
    
    print('Punto 1')
    paises = agregar_pais(paises)
    
    print('punto 2')
    actualizar_datos_pys(paises)
    
    print('Punto 3, buscar países')
    buscar_pais(paises)
    
    print('punto 4')
    filtrado_paises(paises)
    
    print('Punto 5,ordenar países')
    ordenar_paises(paises)
    print(paises)
    
    print("punto 6")
    mostrar_estadisticas(paises)
    
    print('Guardo países en el csv')
    guardar_datos(paises)
    print(paises)