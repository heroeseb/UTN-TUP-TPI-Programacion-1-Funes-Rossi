import csv
import os
import questionary
csv_ruta = 'paises.csv'
paises = []

# Nuevas clases de errores personalizados
class VariableVaciaError(Exception):
    '''Crea una excepción que se utiliza en caso de que la variable tenga el tipo None.'''
    pass

class NombreDuplicadoError(Exception):
    '''Se utiliza en el caso de que el nombre ya esté cargado en la lista.'''
    pass

class NoInicializadaError(Exception):
    '''Se utiliza en el caso de que la lista esté vacía y no haya sido inicializada.'''
    pass

class NoEncontradoError(Exception):
    '''Se utiliza en el caso de que, tras una comparación de valores, no se encuentren coincidencias.'''
    pass

class NumeroNegativoError(Exception):
    ''' En el caso de que se encuentre un número negativo en la validación'''
    pass

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
def seleccionar_menu(mensaje,opciones):
    opcion = questionary.select(
        message= mensaje,
        choices= opciones
    ).ask()
    return opcion

# Función desea continuar con la carga
def desea_continuar():
    continuar = questionary.select(
        message= '¿Desea continuar con la carga?: ',
        choices= ['Si','No']
    ).ask()
    return True if continuar == 'Si' else False

# Función de input con cancelación
def input_c_cancel(mensaje,mensaje_error='Inserte un valor valido.',tipo='str',mensaje_negativo='¡El número debe ser mayor a cero!'):
    match tipo:
        case 'int':
            while True:
                dato = input(mensaje).strip()
                try:
                    numero = int(dato)
                    if numero > 0:
                        return numero
                    else:
                        raise NumeroNegativoError(mensaje_negativo)
                except ValueError:
                    print(mensaje_error)
                except NumeroNegativoError as e:
                    print(e)
                if not desea_continuar():
                    return None
        case 'str':
            while True:
                dato = input(mensaje).strip()
                try:
                    if not dato.replace(' ', '').isalpha() or dato == "":
                        raise ValueError
                    return dato.capitalize()
                except ValueError:
                    print(mensaje_error)
                if not desea_continuar():
                    return None

# Punto 1
def agregar_pais(lista):
    try:
        continentes = {'africa':'África','america':'América','antartida':'Antártida','asia':'Asia','europa':'Europa','oceania':'Oceanía'}
        nombre = input_c_cancel('Ingrese el nombre del país: ', '¡Ingrese un nombre válido','str')
        if nombre == None: raise VariableVaciaError('Se cancelo la carga del país.')
        if quitar_tildes(nombre) in [quitar_tildes(e['nombre']) for e in lista]: raise NombreDuplicadoError('¡El país ya esta cargado en la lista!')
        poblacion = input_c_cancel('Ingrese la cantidad de población: ', '¡Ingrese una cantidad válida!','int')
        if poblacion == None: raise VariableVaciaError('Se cancelo la carga del país.')
        superficie = input_c_cancel('Ingrese la superficie del país: ', '¡Ingrese un número válido!','int')
        if superficie == None: raise VariableVaciaError('Se cancelo la carga del país.')
        continente = input_c_cancel('Ingrese el continente al que pertenece el país: ', 'Ingrese un continente válido.','str')
        if continente == None: raise VariableVaciaError('Se cancelo la carga del país.')
        while not(quitar_tildes(continente) in continentes.keys()):
            print('Por favor ingrese un continente válido.')
            continente = input_c_cancel('Ingrese el continente al que pertenece el país: ', 'Ingrese un continente válido.','str')
            if continente == None: raise VariableVaciaError('Se cancelo la carga del país.')
        if not (nombre and poblacion and superficie and continente): raise VariableVaciaError('¡Faltan datos o se cargaron incorrectamente los datos...!')
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
    except VariableVaciaError as e:
        print(e)
    except NombreDuplicadoError as e:
        print(e)

# punto 2
def actualizar_datos_pys(paises):
    try:
        if not paises:
            raise NoInicializadaError('No hay datos cargados para actualizar.')
        encontrado = False
        pais_actu = input_c_cancel("¿Cual país desea actualizar?: ","Inserte un nombre que se encuentre en la lista.","str")
        for d in paises:
            if pais_actu == d["nombre"]:
                encontrado = True  
                nv_poblacion = input_c_cancel(f"¿Cual sera la nueva poblacion para {pais_actu}?: ","Inserte un valor valido.","int","La cantidad de poblacion debe ser un valor numerico mayor a cero.")
                nv_superficie = input_c_cancel(f"¿Cual sera la nueva superficie para {pais_actu}?: ", "Inserte un valor valido.","int", "La cantidad de superficie debe ser un valor numerico mayor a cero.")
                if nv_poblacion and nv_superficie:
                    d["poblacion"] = nv_poblacion 
                    d["superficie"] = nv_superficie
                    print("País actualizado correctamente.")
        if not (pais_actu and nv_poblacion and nv_superficie): raise VariableVaciaError("Se cancela la actualización de datos")
        if not encontrado: raise NoEncontradoError("No se encontro el país...")
        return paises
    except NoInicializadaError as e:
        print(e)
    except NoEncontradoError as e:
        print(e)
    except VariableVaciaError as e:
        print(e)

# Punto 3
def buscar_pais(lista):
    '''Buscar un país por nombre (coincidencia parcial o exacta).'''
    try:
        if not lista:
            raise NoInicializadaError('No hay datos cargados para buscar.')
        encontro_coincidencia = False
        nombre = input_c_cancel('Ingrese el nombre del país que desea buscar: ', 'Ingrese un nombre válido.','str')
        if nombre == None:
            raise VariableVaciaError('Se cancelo la busqueda')
        for i in range(len(lista)):
            nombre_lista = lista[i]['nombre']
            if quitar_tildes(nombre) in quitar_tildes(nombre_lista):
                if quitar_tildes(nombre[0]) == quitar_tildes(nombre_lista[0]):
                    encontro_coincidencia = True
                    print(f"Nombre del país: {lista[i]['nombre']} | Población: {lista[i]['poblacion']} | Superficie: {lista[i]['superficie']} | Continente: {lista[i]['continente']}")
        if not encontro_coincidencia:
            raise NoEncontradoError('No se encontraron coincidencias.')
    except NoInicializadaError as e:
        print(e)
    except NoEncontradoError as e:
        print(e)
    except VariableVaciaError as e:
        print(e)

# punto 4
def filtrado_paises(paises):
    try:
        if not paises:
            raise NoInicializadaError('No hay datos cargados para filtrar.')
        opcion = seleccionar_menu("Eliga el filtro:",['1) Continente;','2) Rango de población;','3) Rango de superficie;','4) Volver atras.'])[0]
        match opcion:
            case "1":
                encontrado = False
                filtro = seleccionar_menu("Seleccione el continente: ",["África", "América", "Antártida", "Asia", "Europa", "Oceanía"])
                for d in paises:
                    if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.")
                if not encontrado: raise NoEncontradoError("No hay ningun país con ese continente.")
            case "2":
                encontrado = False
                filtro = input_c_cancel("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.")
                if filtro == None:
                    raise VariableVaciaError('Se cancelo el filtrado de países.')
                filtro2 = input_c_cancel("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.")
                if filtro2 == None:
                    raise VariableVaciaError('Se cancelo el filtrado de países.')
                for d in paises:
                    if filtro <= d["poblacion"] and d["poblacion"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.")
                if not encontrado: raise NoEncontradoError("No hay ningun país que coincida con ese rango de población.")
            case "3":
                encontrado = False
                filtro = input_c_cancel("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.")
                if filtro == None:
                    raise VariableVaciaError('Se cancelo el filtrado de países.')
                filtro2 = input_c_cancel("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.")
                if filtro2 == None:
                    raise VariableVaciaError('Se cancelo el filtrado de países.')
                for d in paises:
                    if filtro <= d["superficie"] and d["superficie"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.")
                if not encontrado: raise NoEncontradoError("No hay ningun país que coincida con ese rango de superficie.")
            case "4":
                print("Volviendo...")
            case _:
                print("Eliga una opción presentada en pantalla.")
    except NoInicializadaError as e:
        print(e)
    except NoEncontradoError as e:
        print(e)
    except VariableVaciaError as e:
        print(e)


# Punto 5
def mostrar_todos_paises(lista):
    opcion = seleccionar_menu('¿Desea mostrar todos los países?:',['1. Si','2. No'])
    match opcion[0]:
        case '1':
            for pais in lista:
                print('-'*50)
                for k,v in pais.items():
                    print(f'{k} : {v}')
                print('-'*50)
        case '2':
            return

def ordenar_paises(lista):
    try:
        if not lista:
            raise NoInicializadaError('No hay datos cargados para ordenar.')
        opcion = seleccionar_menu('Ordenar países por:',['1. Nombre','2. Población','3. Superficie','4. Volver al menú principal'])[0]
        match opcion:
            case '1':
                opcion1 = seleccionar_menu('Ordenar de forma:',['1. Ascendente','2. Descendente','3. Volver al menú principal'])[0]
                match opcion1:
                    case '1':
                        lista.sort(key= lambda x:x['nombre'])
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '2':
                        lista.sort(key= lambda x:x['nombre'],reverse=True)
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '3':
                        print('Volviendo al menú principal')
            case '2':
                opcion2 = seleccionar_menu('Ordenar de forma:',['1. Ascendente','2. Descendente','3. Volver al menú principal'])[0]
                match opcion2:
                    case '1':
                        lista.sort(key= lambda x:x['poblacion'])
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '2':
                        lista.sort(key= lambda x:x['poblacion'],reverse=True)
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '3':
                        print('Volviendo al menú principal')
            case '3':
                opcion3 = seleccionar_menu('Ordenar de forma:',['1. Ascendente','2. Descendente','3. Volver al menú principal'])[0]
                match opcion3:
                    case '1':
                        lista.sort(key= lambda x:x['superficie'])
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '2':
                        lista.sort(key= lambda x:x['superficie'],reverse=True)
                        print('¡Países ordenados correctamente!')
                        mostrar_todos_paises(lista)
                    case '3':
                        print('Volviendo al menú principal')
            case '4':
                print('Volviendo al menú principal')
        return lista
    except NoInicializadaError as e:
        print(e)

# punto 6
def mostrar_estadisticas(paises):
    try:
        if not paises:
            raise NoInicializadaError("No hay datos cargados para calcular estadísticas.")
        lista_poblaciones = list(map(lambda x: x["poblacion"], paises))
        lista_superficie = list(map(lambda x: x["superficie"], paises))
        mayor = max(lista_poblaciones)
        menor = min(lista_poblaciones)
        for d in paises:
            if mayor == d["poblacion"]: pais_ma = d["nombre"]
            if menor == d["poblacion"]: pais_me = d["nombre"]
        print(f"""
El país con mayor población es: {pais_ma}, con una cantidad de: {mayor} habitantes.
El país con menor población es: {pais_me}, con una cantidad de: {menor} habitantes.""")
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
    except NoInicializadaError as e:
        print(e)


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