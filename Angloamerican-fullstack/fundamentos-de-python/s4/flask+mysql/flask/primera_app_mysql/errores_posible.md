# Errores 

## Errores posibles

### 1. Error autenticacion

#### Revisar los datos de autenticacion en el archivo `mysqlconnection.py`

- usuario
- password

### 2. Error de coneccion a la base de datos

#### Revisar nombre de base de datos en archivo `mascota.py` en este caso o 'modelo.py' para otros

OperationalError pymsql.err.OperationalErorr:(1049, "Unknown database 'nombre_de_base_de_datos'")

Revisar el nombre de base de datos en el archvio modelo.py

### 3. Error de password

#### Revisar la contraseña par a saber si esta buena.
pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
