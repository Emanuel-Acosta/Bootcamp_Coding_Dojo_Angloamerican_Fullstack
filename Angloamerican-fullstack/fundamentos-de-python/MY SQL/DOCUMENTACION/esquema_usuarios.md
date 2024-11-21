# practica esquema de usuarios :

## Crea 3 nuevos usuarios:
```
insert into usuarios(nombre,apellido,email) values ('user1','Uno','uno@gmail.com');

insert into usuarios(nombre,apellido,email) values ('user2','Dos','Dos@gmail.com');

insert into usuarios(nombre,apellido,email) values ('user3','Tres','Tres@hotmail.com');
```

## Recupera todos los usuarios:

```
select * from esquema_usuarios.usuarios;
+----+--------+----------+------------------+---------------------+---------------------+
| id | nombre | apellido | email            | created_at          | updated_at          |
+----+--------+----------+------------------+---------------------+---------------------+
|  1 | user1  | Uno      | uno@gmail.com    | 2024-11-15 13:46:31 | 2024-11-15 13:51:30 |
|  2 | user2  | Dos      | Dos@gmail.com    | 2024-11-15 13:48:03 | 2024-11-15 13:51:30 |
|  3 | user3  | Tres     | Tres@hotmail.com | 2024-11-15 13:48:03 | 2024-11-15 13:51:30 |
+----+--------+----------+------------------+---------------------+---------------------+
```
## Recupera el primer usuario utilizando la columna de email como condicional
```
select * from usuarios where email = 'uno@gmail.com';
+----+--------+----------+---------------+---------------------+---------------------+
| id | nombre | apellido | email         | created_at          | updated_at          |
+----+--------+----------+---------------+---------------------+---------------------+
|  1 | user1  | Uno      | uno@gmail.com | 2024-11-15 13:46:31 | 2024-11-15 13:51:30 |
+----+--------+----------+---------------+---------------------+---------------------+
```

## Recupera el último usuario utilizando la columna id como condicional
```
select * from usuarios where id = 3
o tambien:
select * from usuarios
     where id = (select max(id) from usuarios);
+----+--------+----------+------------------+---------------------+---------------------+
| id | nombre | apellido | email            | created_at          | updated_at          |
+----+--------+----------+------------------+---------------------+---------------------+
|  3 | user3  | Tres     | Tres@hotmail.com | 2024-11-15 13:48:03 | 2024-11-15 13:51:30 |
+----+--------+----------+------------------+---------------------+---------------------+
```

## Cambia el usuario con id 2 para que su nombre sea “Miu”
```
update usuarios set nombre = 'Miu' where id = 2;
select id, nombre from usuarios where id = 2;
+----+--------+
| id | nombre |
+----+--------+
|  2 | Miu    |
+----+--------+
```

## Elimina el usuario con id 3 de la tabla
```
delete from usuarios where id = 3;
select * from usuarios;
+----+--------+----------+---------------+---------------------+---------------------+
| id | nombre | apellido | email         | created_at          | updated_at          |
+----+--------+----------+---------------+---------------------+---------------------+
|  1 | user1  | Uno      | uno@gmail.com | 2024-11-15 13:46:31 | 2024-11-15 13:51:30 |
|  2 | Miu    | Dos      | Dos@gmail.com | 2024-11-15 13:48:03 | 2024-11-15 14:59:59 |
+----+--------+----------+---------------+---------------------+---------------------+
```

## Obtén todos los usuarios, ordenados por su apellido
```
select * from usuarios order by apellido;
+----+--------+----------+---------------+---------------------+---------------------+
| id | nombre | apellido | email         | created_at          | updated_at          |
+----+--------+----------+---------------+---------------------+---------------------+
|  2 | Miu    | Dos      | Dos@gmail.com | 2024-11-15 13:48:03 | 2024-11-15 14:59:59 |
|  1 | user1  | Uno      | uno@gmail.com | 2024-11-15 13:46:31 | 2024-11-15 13:51:30 |
+----+--------+----------+---------------+---------------------+---------------------+
```

## Obtén todos los usuarios ordenados por su nombre de manera descendente
```
select * from usuarios order by nombre desc;
+----+--------+----------+---------------+---------------------+---------------------+
| id | nombre | apellido | email         | created_at          | updated_at          |
+----+--------+----------+---------------+---------------------+---------------------+
|  1 | user1  | Uno      | uno@gmail.com | 2024-11-15 13:46:31 | 2024-11-15 13:51:30 |
|  2 | Miu    | Dos      | Dos@gmail.com | 2024-11-15 13:48:03 | 2024-11-15 14:59:59 |
+----+--------+----------+---------------+---------------------+---------------------+
```
