# Proyecto Lenguajes de Programación y Código Limpio

## ¿Quién hizo esto?
- **Julio Ochoa**
- **Emanuel Bedoya**

## ¿Qué es y para qué es?
El proyecto consiste en un conjunto de funciones y pruebas unitarias en Python para el desarrollo del juego Batalla Naval. Su propósito es proporcionar al usuario un tablero del juego Batalla Navala, el cuál se lleva a cabo con dos jugadores y éste mismo permite cargar, guardar y eliminar las partidas realizadas.

## ¿Cómo lo hago funcionar?

### Prerrequisitos:
- Python instalado en el sistema.
- Instalar flask con el comando: `pip install flask`
- Crear una base de datos PostgreSQL y configurar los respectivos datos de acceso.
- Instalar psycopg2 con el comando: `pip install psycopg2`
- Buscar el archivo `tabla.sql` en la carpeta sql, copiar su contenido y correrlo en el sql editor de su base de datos NEON


## ¿Cómo está hecho?
El proyecto está implementado en Python con interfaz gráfica, conexion a base de datos y conexión a una página desarrollada en HTML. La estructura del proyecto incluye:

### Componentes:

### Pruebas unitarias:
- **testjuego.py**:
  - Utilizan el módulo `unittest` de Python para realizar pruebas automatizadas de las funcion de crear el tablero.

- **testBD.py**:
  - Proporciona una prueba de los métodos para eliminar partida, guardar partida, consultar numero de partidas existentes y las excepciones para cada una de ellas.

### Organización de los módulos:
- **src**:
  - Contiene la carpeta `Controller` donde se encuentra el archivo `Control.py`.
  - Contiene la carpeta `GUI` donde se encuentra el archivo `interfazz.py`.
  - Contiene la carpeta `Model` donde se encuentran los archivos `Juego_principal.py` y `Logica.py`.
- **tests**:
  - Contiene el archivo `testBD.py`.
  - Contiene el archivo `testjuego.py`.
- **web**:
  - Contiene la carpeta `Templates` donde se encuentran los archivos `index.html` y `partidas.html`.
  - Contiene el archivo `app.py`.
## Uso

Para ejecutas la consola , desde la carpeta del programa , use el comando.

 `Batallanaval>python src/Model/Juego_principal.py`

Para ejecutar las pruebas unitarias, desde la carpeta del programa, use el comando.

`Batallanaval>python test/testBD.py`

Para ejecutar la página web, desde la carpeta del programa, use el comando.

`Batallanaval>python web/app.py`

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas.


  `import sys` 
  `sys.path.append("src")`



## Database-MVC.

### Requisitos:

### Configuración de la base de datos:
Esta aplicación requiere que esté creada una tabla llamada Archivos. Utilice el script en `sql/tabla.sql` para crearla antes de ejecutar la aplicación.

Asegúrese de tener una base de datos PostgreSQL y sus respectivos datos de acceso. Modifique el archivo `SecretConfig-Sample.py` a `SecretConfig.py` e ingrese en este archivo los datos de conexión a su base de datos.

Establezca el puerto 5432 que es por defecto.

-PGHOST='xxx'

-PGDATABASE='xxxx'

-PGUSER='xxxxx'

-PGPASSWORD='xxx'

-PGPORT = 'xxx'





