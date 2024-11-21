SELECT de toda la tabla
Para ver todas las columnas de una tabla utilizamos el siguiente query:

o	usuarios
SELECT *

FROM usuarios;


	SELECT de ciertas columnas
Para seleccionar ciertas columnas de una tabla reemplazamos el asterisco (*) por el nombre de las columnas que queremos mostrar separados por coma (,):
	
o	nombre de tabla de usuarios
SELECT nombre

FROM usuarios;

	SELECT con condicionales
Para restringir nuestra búsqueda utilizaremos la palabra reservada WHERE seguido de la condicional que queremos para la consulta. A continuación algunos ejemplos:
	
o	Para obtener el nombre del usuario con id de 5:
SELECT nombre

FROM usuarios

WHERE id = 5;
	
o	Para obtener el apellido de los usuario con id de 4 y 5:
SELECT nombre

FROM usuarios

WHERE id = 4 OR id = 5;
	
o	Para obtener todas las columnas de los usuarios cuyo id es mayor a 3:
SELECT *

FROM usuarios

WHERE id > 3;
	
o	Para obtener todas las columnas de los usuarios con id menor o igual a 4:
SELECT *

FROM usuarios

WHERE id <= 4;
	
o	Para obtener la fecha de nacimiento de los usuarios con id distinto a 3:
SELECT *

FROM usuarios

WHERE id != 3;
	
o	Para obtener todas las columnas de los usuarios con nombres que terminan en ‘e’. Para esta consulta usaremos %, que actuará como comodín:
SELECT *

FROM usuarios

WHERE nombre LIKE '%e';
	
o	Para obtener todas las columnas de los usuarios con nombre_usuario que comienza en ‘r’. De nuevo usaremos %:
SELECT *

FROM usuarios

WHERE nombre_usuario LIKE 'r%';
	
o	Para obtener todas las columnas de los usuarios que no comienzan con ‘A’. Usaremos la sentencia NOT:
SELECT *

FROM usuarios

WHERE nombre NOT LIKE 'A%';
 
	SELECT con ordenamiento
Para tener un orden en la información que recuperamos usamos la sentencia ORDER BY seguido de la columna en la cual nos basamos para ordenar y si queremos mostrar la información de manera ascendente (ASC) o descendente (DESC). A continuación algunos ejemplos:
	
	Para obtener todos los tweets ordenados por fecha de creación (created_at), mostrando los más antiguos primero:
SELECT * FROM tweets

ORDER BY created_at ASC;
	
o	Para obtener todos los tweets ordenados por fecha de creación (created_at), mostrando los más recientes primero:
SELECT * FROM tweets

ORDER BY created_at DESC;
	
o	Para obtener todos los tweets que incluyan la palabra ‘navidad’, ordenados por fecha de creación (created_at), mostrando los más recientes primero
SELECT * FROM tweets

WHERE tweet LIKE '%navidad%'

ORDER BY created_at DESC;
	
o	Para obtener todos los nombres de usuarios en orden alfabético:
SELECT nombre

FROM usuarios

ORDER BY nombre;
Por defecto, ORDER BY ordena de forma ASC (ascendente) por lo que podemos ignorar esa parte si queremos ordenar de esta manera.
 
	SELECT con LÍMITE y DESPLAZAMIENTO
Podemos restringir la cantidad de registros que nos regresa una consulta con la sentencia LIMIT y “desplazar” para que comience a partir de un índice con OFFSET. A continuación algunos ejemplos:
	
o	Para obtener los primeros 3 tweets:
SELECT *

FROM tweets

LIMIT 3;
	
o	Para obtener los tweets de 3-5. A través de LIMIT indicamos que solo nos regrese 3 registros, con OFFSET establecemos en qué índice comenzará (recuerda que contamos a partir del 0):
SELECT *

FROM tweets

LIMIT 3

OFFSET 2;
	
o	También podemos combinar LIMIT y OFFSET con la siguiente sintaxis, donde el primer número se refiere al desplazamiento y el segundo al límite:
SELECT *

FROM tweets

LIMIT 2, 3;
