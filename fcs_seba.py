import csv
csv_ruta = 'paises.csv'
paises = []
def cargar_datos(ruta):
    paises = []
    try:
        with open(ruta,'r',encoding='utf-8',newline='') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    fila['nombre'] = fila['nombre']
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    fila['continente'] = fila['continente']
                    paises.append(fila)
                except (ValueError,KeyError,TypeError):
                    print('Se ignoro una linea invalida del CSV')
    except FileNotFoundError:
        print('El archivo no existe. Se creará una lista vacía.')
    except PermissionError:
        print('Error... No tenes permiso de lectura en este archivo.')
    return paises

def input_str(mensaje,mensaje_2=None):
    while True:
        try:
            input_salid = input(mensaje).strip()
            if not input_salid.replace(' ','').isalpha():
                raise TypeError
            return input_salid
        except TypeError:
            print(mensaje_2 if mensaje_2 else 'Error de tipo')


def input_int(mensaje,mensaje_2=None):
    while True:
        try:
            input_salid = int(input(mensaje))
            return input_salid
        except ValueError:
            print(mensaje_2 if mensaje_2 else 'Error de valor')

def agregar_producto(lista):
    nombre = input_str('Ingrese el nombre del pais: ','Ingrese un nombre valido')
    poblacion = input_int('Ingrese la cantidad de población: ','Ingrese una cantidad válida!')
    while not poblacion > 0:
        print('El numero debe ser mayor a cero!')
        poblacion = input_int('Ingrese la cantidad de población: ','Ingrese una cantidad válida!')
    superficie = input_int('Ingrese la superficie del pais: ','Ingrese un número valido!')
    while not superficie > 0:
        print('La superficie debe ser mayor a cero!')
        superficie = input_int('Ingrese la superficie del pais: ','Ingrese un número valido!')
    continente = input_str('Ingrese el continen al que pertenece el pais: ','Ingrese un continente valido')
    if not(nombre and poblacion and superficie and continente):
        print ('Faltan datos/se cargaron incorrectamente los datos!...')
    else:
        diccionario = {
                        'nombre': nombre.capitalize(),
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': continente.capitalize()}
        lista.append(diccionario)
        print('Se agrego correctamente el pais!')
    return lista


if __name__ == '__main__':
    print('iniciamos lista y cargamos datos')
    paises = cargar_datos(csv_ruta)
    print(paises)
    print('punto 1')
    paises = agregar_producto(paises)
    print(paises)