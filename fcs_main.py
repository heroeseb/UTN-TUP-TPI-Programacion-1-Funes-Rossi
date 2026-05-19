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

if __name__ == '__main__':
    paises = cargar_datos(csv_ruta)
    print(paises)
