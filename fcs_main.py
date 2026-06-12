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
    '''Lee el archivo CSV de países y carga sus datos en una lista de diccionarios, validando los tipos de datos.'''
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
    '''Guarda la lista actual de países en el archivo CSV especificado en la ruta.'''
    try:
        with open(csv_ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=Fieldnames)
            writer.writeheader()
            writer.writerows(lista)
            print('Se guardaron correctamente los datos.')
    except PermissionError:
        print('¡Error! No se pudo guardar. El archivo está abierto por otro programa o no hay permisos.')

# Limpiar consola
def limpiar_consola():
    '''Limpia la pantalla de la consola adaptándose al sistema operativo en uso.'''
    os.system('cls' if os.name == 'nt' else 'clear') # basicamente elimina todo lo escrito anteriormente en la consola. La limpia visualmente.

# Función para continuar
def continuar():
    '''Pausa la ejecución del programa hasta que el usuario presione la tecla Enter.'''
    input("Presione ¬Enter para continuar") # cualquer cosa que ponga el usuario, va a continuar. 

# funcion para quitar tildes
def quitar_tildes(texto): # basicamente cambia las letras que llevan tildes por letras que no tengan tildes.
    '''Convierte el texto a minúsculas y reemplaza las vocales con tilde y caracteres especiales por sus versiones normales.'''
    texto = texto.lower() # primero lo vuelve todo minusculas
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
        texto = texto.replace(letra_tilde, letra_normal) # aca las reemplaza
    return texto # devuelve el texto ingresado, pero sin tildes


# Seleccionar con questionary
def seleccionar_menu(mensaje,opciones):
    '''Despliega un menú interactivo utilizando la librería questionary y retorna la opción seleccionada.'''
    opcion = questionary.select( # Opcion es una variable que toma el dato que devuelve .select()
        message= mensaje, # message es el mensaje de aparece primero, pero que no se selecciona
        choices= opciones # choices son las opciones que el usuario puede seleccionar 
    ).ask() # .ask() define que es una pregunta, algo que debe de devolver.
    return opcion # devuelve "opcion"

# Función desea continuar con la carga
def desea_continuar():
    '''Pregunta al usuario si desea continuar con el proceso actual y retorna True o False según corresponda.'''
    continuar = questionary.select( # continuar es una variable que toma el dato que devuelve .select()
        message= '¿Desea continuar con la carga?: ', # message es el mensaje de aparece primero, pero que no se selecciona
        choices= ['Si','No'] # choices son las opciones que el usuario puede seleccionar 
    ).ask() # .ask() define que es una pregunta, algo que debe de devolver.
    return True if continuar == 'Si' else False # si continuar es igual a "Si" una opcion que puede seleccionar el usuario, entonces se devuelve True. De lo contrario se devuelve False

# Función de input con cancelación
def input_c_cancel(mensaje,mensaje_error='Inserte un valor valido.',tipo='str',mensaje_negativo='¡El número debe ser mayor a cero!'):
    '''Solicita una entrada por teclado validando si es de tipo entero (positivo) o cadena de texto, permitiendo cancelar.'''
    match tipo:
        case 'int': # Si esperamos que sea int el dato devuelto
            while True:
                dato = input(mensaje).strip() # dato es la variable que se devuelve
                try:
                    numero = int(dato)
                    if numero > 0: # si numero es mayor que cero
                        return numero
                    else:
                        raise NumeroNegativoError(mensaje_negativo) # Salta el error de numero negativo
                except ValueError: # Si el dato no es un numero o caracter valido para int
                    print(mensaje_error)
                except NumeroNegativoError as e: # error de que si es negativo el numero
                    print(e)
                if not desea_continuar(): # se cita la funcion. Caso de devolver False:
                    return None # no se returnea nada.
        case 'str': # Si esperamos que sea string el dato devuelto
            while True:
                dato = input(mensaje).strip() # Sacamos los espacios del principio y final con el .strip()
                try:
                    if not dato.replace(' ', '').isalpha() or dato == "": # Nos fijamos que no sea un espacio o no sea nada la variable. 
                        raise ValueError # salta el error de ValueError
                    return dato.capitalize()
                except ValueError: # Si el dato no es una letra o caracter valido para string
                    print(mensaje_error) # printea el mensaje_error. 
                if not desea_continuar(): # se cita la funcion con el mismo nombre. Caso de devolver False:
                    return None # no se returnea nada

# Punto 1
def agregar_pais(lista):
    '''Pide los datos de un nuevo país por consola, los valida, verifica que no esté duplicado y lo agrega a la lista.'''
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
    '''Busca un país determinado por su nombre y permite actualizar sus valores de población y superficie.'''
    try: # abrimos try. para despues saltar los errores si es que surgen.
        if not paises:
            raise NoInicializadaError('No hay datos cargados para actualizar.') # Si la lista paises no esta creada o no tiene datos dentro. Salta el error.
        encontrado = False # Una bandera.
        pais_actu = input_c_cancel("¿Cual país desea actualizar?: ","Inserte un nombre que se encuentre en la lista.","str")
        if pais_actu == None: raise VariableVaciaError("Se cancela la actualización de datos") # Por si no ingresa nada el usuario.
        for d in paises:
            if pais_actu == d["nombre"]: # d["nombre"] es el nombre del respectivo pais.
                encontrado = True  # Aca esta la bandera, si esta true, sabemos que si se encontro algo.
                nv_poblacion = input_c_cancel(f"¿Cual sera la nueva poblacion para {pais_actu}?: ","Inserte un valor valido.","int","La cantidad de poblacion debe ser un valor numerico mayor a cero.")
                if nv_poblacion == None: raise VariableVaciaError("Se cancela la actualización de datos") # Por si no ingresa nada el usuario.
                nv_superficie = input_c_cancel(f"¿Cual sera la nueva superficie para {pais_actu}?: ", "Inserte un valor valido.","int", "La cantidad de superficie debe ser un valor numerico mayor a cero.")
                if nv_superficie == None: raise VariableVaciaError("Se cancela la actualización de datos") # Por si no ingresa nada el usuario.
                if nv_poblacion and nv_superficie:
                    d["poblacion"] = nv_poblacion 
                    d["superficie"] = nv_superficie # Aca se cambian los valores, por los nuevos.
                    print("País actualizado correctamente.")
        if not encontrado: raise NoEncontradoError("No se encontro el país...") # Aca la bandera, por si no se encontro ningun pais. Salta el error de noencotnrado
        return paises
    except NoInicializadaError as e: # Error de que paises esta vacia
        print(e)
    except NoEncontradoError as e: # Error de que no se encontro nada
        print(e)
    except VariableVaciaError as e: # Error de que la variable esta vacia
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
    '''Muestra un menú para filtrar y listar países según continente, rangos de población o rangos de superficie.'''
    try: # abrimos try. para despues saltar los errores si es que surgen.
        if not paises:
            raise NoInicializadaError('No hay datos cargados para filtrar.') # Si la lista paises no esta creada o no tiene datos dentro. Salta el error.
        opcion = seleccionar_menu("Eliga el filtro:",['1) Continente;','2) Rango de población;','3) Rango de superficie;','4) Volver atras.'])[0] # Usamos la funcion questionary para que el usuario eliga la opcion de filtrado.
        match opcion: # match con la variable devuelta "opcion"
            case "1": # continente
                encontrado = False # banderita
                filtro = seleccionar_menu("Seleccione el continente: ",["África", "América", "Antártida", "Asia", "Europa", "Oceanía"]) # Otro menu más para que seleccione el continente filtro
                for d in paises: # un for para recorrer la lista
                    if filtro == d["continente"]: encontrado = True , print(f"-{d["nombre"]}.") # Si el continente de ese pais es el mismo que el seleccionado. Lo printeamos y cambiamos la banderita a True.
                if not encontrado: raise NoEncontradoError("No hay ningun país con ese continente.") # en el caso de que la banderita no cambie, salta error.
            case "2": # rango de poblacion
                encontrado = False # banderita
                filtro = input_c_cancel("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.") # El inicio del rango
                if filtro == None: # Si la variable no existe:
                    raise VariableVaciaError('Se cancelo el filtrado de países.') # salta error
                filtro2 = input_c_cancel("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.") # El final del rango
                if filtro2 == None: # Si la variable no existe:
                    raise VariableVaciaError('Se cancelo el filtrado de países.') # salta error
                for d in paises: # un for para recorrer la lista
                    if filtro <= d["poblacion"] and d["poblacion"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.") # Buscamos si la poblacion del pais entra dentro del rango. cambiamos la banderita a True y printeamos el pais.
                if not encontrado: raise NoEncontradoError("No hay ningun país que coincida con ese rango de población.") # en el caso de que la banderita no cambie, salta error.
            case "3": # rango de superficie
                encontrado = False # banderita
                filtro = input_c_cancel("Ingrese el comienzo del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.") # El inicio del rango
                if filtro == None: # Si la variable no existe:
                    raise VariableVaciaError('Se cancelo el filtrado de países.') # salta error
                filtro2 = input_c_cancel("Ingrese el final del rango: ","Trate de ingresar un valor numerico valido.","int","La cantidad debe ser mayor a cero. Minimo 1.") # El final del rango
                if filtro2 == None: # Si la variable no existe:
                    raise VariableVaciaError('Se cancelo el filtrado de países.') # salta error
                for d in paises: # un for para recorrer la lista
                    if filtro <= d["superficie"] and d["superficie"] <= filtro2: encontrado = True , print(f"-{d["nombre"]}.") # Buscamos si la superficie del pais entra dentro del rango. Cambiamos la banderita a True y printeamos el pais.
                if not encontrado: raise NoEncontradoError("No hay ningun país que coincida con ese rango de superficie.") # en el caso de que la banderita no cambie, salta error.
            case "4": # Nos vamos al menu principal
                print("Volviendo...")
            case _: # Por si surge un error desconocido.
                print("Eliga una opción presentada en pantalla.")
    except NoInicializadaError as e: # Error de que paises esta vacia
        print(e)
    except NoEncontradoError as e: # Error de que no se encontro nada
        print(e)
    except VariableVaciaError as e: # Error de que la variable esta vacia
        print(e)


# Punto 5
def mostrar_todos_paises(lista):
    '''Le pregunta al usuario si desea visualizar todos los países y, en caso afirmativo, los imprime estructuradamente por consola.'''
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
    '''Ordena la lista de países por nombre, población o superficie de forma ascendente o descendente según el usuario elija.'''
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
    '''Calcula y muestra estadísticas generales como promedios, máximos, mínimos de población y cantidad de países por continente.'''
    try: # abrimos try. para despues saltar los errores si es que surgen.
        if not paises:
            raise NoInicializadaError("No hay datos cargados para calcular estadísticas.") # Si la lista paises no esta creada o no tiene datos dentro. Salta el error.
        lista_poblaciones = list(map(lambda x: x["poblacion"], paises)) # list sirve para crear una lista. Uso lambda para agarrar cada dato de pooblacion y lo agrego a lista_poblaciones.
        lista_superficie = list(map(lambda x: x["superficie"], paises)) # list(map)(lambda "variable temporal": variable temporal["clave de los diccionarios"], nombre de la lista). Aca hacemos lo mismo que poblaciones solo que con superficie
        mayor = max(lista_poblaciones) # con max saco el mayor numero de la lista
        menor = min(lista_poblaciones) # con min saco el menor numero de la lista
        for d in paises: # un for para recorrer la lista
            if mayor == d["poblacion"]: pais_ma = d["nombre"] # buscamos la poblacion que coincida con mayor para guardarlo en otra variable
            if menor == d["poblacion"]: pais_me = d["nombre"] # lo mismo pero con menor
        print(f"""
El país con mayor población es: {pais_ma}, con una cantidad de: {mayor} habitantes.
El país con menor población es: {pais_me}, con una cantidad de: {menor} habitantes.""")# printeamos los datos sacados
        print(f"El promedio de población es: {sum(lista_poblaciones) / len(lista_poblaciones)}.") # printeamos promedios. uso sum para sumar todos los datos de la lista. len para sacar la cantidad de datos dentro de la lista.
        print(f"El promedio de superficie es: {sum(lista_superficie) / len(lista_superficie)}.") # formula promedio: sum(la lista) / len(la lista). Saco promedio de poblacion y despues de superficie.
        americanos = 0
        europeos = 0
        africanos = 0
        asiaticos = 0
        oceanicos = 0 # todas estas variables son un contador de cada continente.
        for d in paises: # un for para recorrer la lista
            if d["continente"] == "América": americanos += 1
            elif d["continente"] == "África": africanos += 1
            elif d["continente"] == "Europa": europeos += 1
            elif d["continente"] == "Asia": asiaticos += 1
            elif d["continente"] == "Oceanía": oceanicos += 1 # aca busco que el continente coincida con el nombre del continente. Cuando coincidan le sumo uno al contador
        print(f"""Cantidad de paises en..:
América: {americanos};
Europa: {europeos};
Asia: {asiaticos};
África: {africanos};
Oceanía: {oceanicos}.""") # aca imprimo los contadores.
    except NoInicializadaError as e: # Error de que paises esta vacia
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