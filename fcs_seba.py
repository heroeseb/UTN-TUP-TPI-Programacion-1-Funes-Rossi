def input_str(mensaje,mensaje_2=None):
    try:
        input_salid = input(mensaje)
        if not input_salid.replace(' ','').isalpha():
            raise TypeError
        return input_salid
    except TypeError:
        print(mensaje_2 if mensaje_2 else 'Error de tipo')


def input_int(mensaje,mensaje_2=None):
    try:
        input_salid = int(input(mensaje))
        return input_salid
    except ValueError:
        print(mensaje_2 if mensaje_2 else 'Error de valor')

def agregar_producto(lista):
    nombre = input_str('Ingrese el nombre del producto: ','Ingrese un nombre valido')
    categoria = input_str('Ingrese la categoria del producto: ','Ingrese una categoria valida')
    precio = input_int('Ingrese el precio del producto: ')
    while not precio > 0:
        print('El precio debe ser mayor a cero!')
        precio = input_int('Ingrese el precio del producto: ')
    stock = input_int('Ingrese el Stock: ')
    while not stock >= 0:
        print('El stock debe ser mayor o igual a cero!')
        stock = input_int('Ingrese el Stock: ')
    if not(nombre and categoria and precio and stock):
        print ('Faltan datos/se cargaron incorrectamente los datos!...')
    else:
        diccionario = {
                        'nombre': nombre,
                        'categoria': categoria,
                        'precio': precio,
                        'stock': stock}
        print('Se agrego correctamente el producto!')
        return diccionario