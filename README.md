# Sistema de Gestión y Análisis de Datos Demográficos Globales

## Descripción del Proyecto

Este proyecto fue desarrollado para la materia **Programación I - UTN** y consiste en un sistema realizado en Python que permite gestionar información demográfica de distintos países almacenada en un archivo CSV.

La aplicación brinda herramientas para cargar, modificar, buscar, filtrar, ordenar y analizar datos de países, incluyendo información como población, superficie y continente al que pertenecen.

Además, incorpora validaciones de datos, manejo de excepciones personalizadas y persistencia de información mediante archivos CSV.

---

## Integrantes

* Integrante 1: Funes Pablo Sebastian
* Integrante 2: Valentino Rossi

---

## Tecnologías Utilizadas

* Python 3
* Módulo `csv`
* Módulo `os`
* Biblioteca `questionary`

---

## Estructura del Proyecto

```
├── main.py
├── fcs_main.py
├── paises.csv
└── README.md
```

### Archivos

* **main.py**: contiene el menú principal y la interacción con el usuario.
* **fcs_main.py**: contiene todas las funciones del sistema.
* **paises.csv**: almacena los datos de los países.
* **README.md**: documentación del proyecto.

---

## Funcionalidades

### 1. Agregar País

Permite ingresar un nuevo país indicando:

* Nombre
* Población
* Superficie
* Continente

El sistema valida que:

* No existan nombres duplicados.
* Los datos sean válidos.
* Los valores numéricos sean mayores que cero.

---

### 2. Actualizar Datos

Permite modificar:

* Población
* Superficie

de un país ya registrado.

---

### 3. Buscar País

Permite buscar países mediante coincidencia total o parcial de su nombre.

---

### 4. Filtrar Países

Se pueden realizar filtros por:

* Continente
* Rango de población
* Rango de superficie

---

### 5. Ordenar Países

Permite ordenar los registros por:

* Nombre
* Población
* Superficie

En forma:

* Ascendente
* Descendente

---

### 6. Estadísticas

El sistema calcula automáticamente:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

## Manejo de Errores

Se implementaron excepciones personalizadas para mejorar la robustez del sistema:

* `VariableVaciaError`
* `NombreDuplicadoError`
* `NoInicializadaError`
* `NoEncontradoError`
* `NumeroNegativoError`

Estas excepciones permiten controlar situaciones como:

* Datos vacíos.
* Países duplicados.
* Búsquedas sin resultados.
* Listas vacías.
* Valores negativos.

---

## Instalación

### 1. Clonar el repositorio

```
git clone https://github.com/usuario/repositorio.git
```

### 2. Ingresar al proyecto

```
cd repositorio
```

### 3. Instalar dependencias

```
pip install questionary
```

### 4. Ejecutar el programa

```
python main.py
```

---

## Formato del Archivo CSV

El archivo debe contener las siguientes columnas:

```
nombre,poblacion,superficie,continente
Argentina,47000000,2780400,América
Brasil,214000000,8515767,América
España,48000000,505990,Europa
```

---

## Ejemplos de Uso

### Ejemplo 1: Agregar un País

#### Entrada

```
Nombre: Chile
Población: 19600000
Superficie: 756102
Continente: América
```

#### Salida

```
¡Se agregó correctamente el país!
```

---

### Ejemplo 2: Buscar un País

#### Entrada

```
Ingrese el nombre del país: Argentina
```

#### Salida

```
Nombre del país: Argentina
Población: 47000000
Superficie: 2780400
Continente: América
```

---

### Ejemplo 3: Filtrar por Continente

#### Entrada

```
Seleccione continente: Europa
```

#### Salida

```
-España
-Francia
-Alemania
```

---

### Ejemplo 4: Mostrar Estadísticas

#### Salida

```
El país con mayor población es: India.
El país con menor población es: Uruguay.

Promedio de población: 55000000
Promedio de superficie: 1200000

Cantidad de países por continente:
América: 5
Europa: 3
Asia: 4
África: 2
Oceanía: 1
```

## Ejemplos de Validación y Manejo de Errores

El sistema incorpora validaciones para evitar datos incorrectos y mantener la integridad de la información.

---

### Error al ingresar texto en un campo numérico

#### Entrada

```
Ingrese la cantidad de población: veinte millones
```

#### Salida

```
¡Ingrese una cantidad válida!
```

---

### Error al ingresar un número negativo

#### Entrada

```
Ingrese la superficie del país: -500
```

#### Salida

```
¡El número debe ser mayor a cero!
```

---

### Error al ingresar un país duplicado

Supongamos que Argentina ya existe en la lista.

#### Entrada

```
Ingrese el nombre del país: Argentina
```

#### Salida

```
¡El país ya está cargado en la lista!
```

---

### Error al ingresar un continente inválido

#### Entrada

```
Ingrese el continente al que pertenece el país: Marte
```

#### Salida

```
Por favor ingrese un continente válido.
```

Los continentes aceptados son:

```
África
América
Antártida
Asia
Europa
Oceanía
```

---

### Error al buscar un país inexistente

#### Entrada

```
Ingrese el nombre del país que desea buscar: Wakanda
```

#### Salida

```
No se encontraron coincidencias.
```

---

### Error al actualizar un país inexistente

#### Entrada

```
¿Cuál país desea actualizar?: Atlantis
```

#### Salida

```
No se encontró el país...
```

---

### Error al filtrar sin resultados

#### Entrada

```
Rango de población:
Desde: 1
Hasta: 5
```

#### Salida

```
No hay ningún país que coincida con ese rango de población.
```

---

### Error al intentar utilizar funciones con la lista vacía

Si el archivo CSV no contiene datos o todavía no se cargó ningún país.

#### Salida al buscar

```
No hay datos cargados para buscar.
```

#### Salida al actualizar

```
No hay datos cargados para actualizar.
```

#### Salida al ordenar

```
No hay datos cargados para ordenar.
```

#### Salida al mostrar estadísticas

```
No hay datos cargados para calcular estadísticas.
```

---

### Cancelación de una operación

El sistema permite cancelar ciertas operaciones cuando el usuario decide no continuar.

#### Salida

```
Se canceló la carga del país.
```

o

```
Se cancela la actualización de datos.
```

---

### Error al abrir o guardar el archivo CSV

#### Si el archivo no existe

```
El archivo no existe. Se creará una lista vacía.
```

#### Si el archivo está abierto o sin permisos

```
¡Error! No se pudo guardar. El archivo está abierto por otro programa o no hay permisos.
```

---

## Objetivos Académicos

Durante el desarrollo de este trabajo práctico se aplicaron conceptos vistos en la materia:

* Funciones.
* Listas y diccionarios.
* Archivos CSV.
* Validación de datos.
* Manejo de excepciones.
* Programación modular.
* Ordenamiento y filtrado de información.
* Expresiones Lambda.
* Uso de bibliotecas externas.
* Persistencia de datos.

---

## Conclusión

Este proyecto permitió desarrollar una aplicación completa de consola para la gestión de información demográfica utilizando Python. Además de reforzar conceptos fundamentales de programación, se trabajó con estructuras de datos, archivos, validaciones y manejo de errores, logrando una solución funcional y organizada siguiendo buenas prácticas de programación.