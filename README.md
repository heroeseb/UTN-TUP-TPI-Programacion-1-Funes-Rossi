# UTN-TUP-TPI-Programacion-1-Funes-Rossi
Sistema en Python para la gestión, filtrado, ordenamiento y análisis estadístico de datos demográficos globales a partir de archivos CSV. Desarrollado para la materia Programación 1 - UTN. Año 2026

(-)Integrantes:
-Funes Pablo
-Rossi Valentino

(-)Instrucciones de desarrollo:
Se nos asigno el desarrollo de un programa en Python que permite gestionar informacion sobre paises, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadisticas. El mismo sistema debe ser capaz de leer un archivo .csv y trabajar con los datos del mismo. El programa debe ser capaz de realizar consultas y general indicadores clave a partir del dataset.

Debemos de usar todo lo aprendido de la materia Programacion 1. (Nos dieron libertad de buscar librerias para uso propio, siempre y cuando esten permitidas).
Temas:
1- Estructuras Secuenciales (Uso de variables string, int, float y bool);
2- Estructuras Condicionales (Uso del if, elif, else y match case);
3- Estructuras Repetitivas (Uso del while y for i in range );
4- Trabajo colaborativo (Uso del GitHub);
5- Listas (Uso de listas como base de datos, sacar provecho de sus indices);
6- Funciones (Uso de como crear las funciones y usarlas);
7- Datos complejos (Manejo de diccionarios, tuplas y sets);
8- Manejo de errores (Uso del try, except, else, y finally);
9- Manejo de archivos (Manejo de archivos como .csv y .txt).

(-)Instrucciones al usuario:
Al iniciar el programa se va a encontrar con el menu. Se le proporciona 7 acciones para realizar, cada una se detalla en su nombre que es lo que hacen.
Para seleccionar la opcion que desea realizar, maneje con las flechas del teclado hasta que la flecha de la izquierda de las opciones este apuntando la opcion que desea hacer. Una vez que la flecha apunte a la opcion: Aprete enter.
Dependiendo de la opcion, se le pedira escribir o seleccionar un submenu. El submenu se maneja igual que el menu principal.
La opcion 7 (salir) le permite salir del programa, si es que así lo desea.
Recuerde usar tildes.

(-)Ejemplos tecnicos:
-Ejemplo N°1:
El usuario ingresa "}", sea acompañado de un texto o no.
Entrada: Alemania}
Salida: ¡Ingrese un valor valido!

-Ejemplo N°2:
Nosotros como desarrolladores nos equivocamos al citar una función:
Entrada: mostrar_estadisticas(lista)
Salida: Un error de que "lista" no es una variable definida. ¿Quiso decir "list"?

-Ejemplo N°3:
El usuario de alguna manera rompe el programa:
Entrada: "El usuario usa programas de terceros"
Salida: El archivo paises.csv no se guarda correctamente, corriendo el riesgo de que se corrompa.

-Ejemplo N°4:
El usuario ingresa nada dentro de un input.
Entrada: un String vacio
Salida: Ingrese un nombre valido.

-Ejemplo N°5:
Al ingresar el continente en un pais nuevo, el usuario pone un continente inexistente.
Entrada: "El pepe"
Salida: "Por favor ingrese un continente válido."

-Ejemplo N°6:
Nosotros como desarrolladores nos olvidamos de guardar el archivo .csv:
Entrada: Cerramos el programa.
Salida: El archivo .csv no se guarda, los datos nuevos se pierden y se quedan los datos anteriores.