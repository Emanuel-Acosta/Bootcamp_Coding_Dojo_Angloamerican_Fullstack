## Crea 3 cursos nuevos:
```
insert into cursos (nombre) values ('Matematica'),('Biologia'),('Fisica');

select * from cursos;
+----+------------+---------------------+---------------------+
| id | nombre     | created_at          | updated_at          |
+----+------------+---------------------+---------------------+
|  1 | Matematica | 2024-11-15 15:39:16 | 2024-11-15 15:39:16 |
|  2 | Biologia   | 2024-11-15 15:39:16 | 2024-11-15 15:39:16 |
|  3 | Fisica     | 2024-11-15 15:39:16 | 2024-11-15 15:39:16 |
+----+------------+---------------------+---------------------+
```

## Elimina los 3 cursos que creaste:
```
delete from cursos;

 select * from cursos;
Empty set 
```

## Crea otros 3 cursos nuevos:
```
insert into cursos (nombre) values ('Ingles'),('Quimica'),('Turismo');

 select * from cursos;
+----+---------+---------------------+---------------------+
| id | nombre  | created_at          | updated_at          |
+----+---------+---------------------+---------------------+
|  4 | Ingles  | 2024-11-15 15:46:43 | 2024-11-15 15:46:43 |
|  5 | Quimica | 2024-11-15 15:46:43 | 2024-11-15 15:46:43 |
|  6 | Turismo | 2024-11-15 15:46:43 | 2024-11-15 15:46:43 |
+----+---------+---------------------+---------------------+
```
## Crea 3 estudiantes que estén inscritos en el primer curso:
```
insert into estudiantes (nombre, apellido, edad, cursos_id ) values ('Antonio','Perez',23, 4);
insert into estudiantes (nombre, apellido, edad, cursos_id ) values ('Xavier','Ruiz',40, 4);
insert into estudiantes (nombre, apellido, edad, cursos_id ) values ('Pedro','Colon',15, 4);

select * from estudiantes;
+----+---------+----------+------+---------------------+---------------------+-----------+
| id | nombre  | apellido | edad | created_at          | updated_at          | curso_id  |
+----+---------+----------+------+---------------------+---------------------+-----------+
|  1 | Antonio | Perez    |   23 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
|  2 | Xavier  | Ruiz     |   40 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
|  3 | Pedro   | Colon    |   15 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
+----+---------+----------+------+---------------------+---------------------+-----------+
```

## Crea 3 estudiantes que estén inscritos en el segundo curso:
```
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Javiera','Marin',67, 5);
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Ricardo','Lopez',35, 5);
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Paola','Reyes',21, 5);

select * from estudiantes where curso_id = 5;
+----+---------+----------+------+---------------------+---------------------+-----------+
| id | nombre  | apellido | edad | created_at          | updated_at          | curso _id |
+----+---------+----------+------+---------------------+---------------------+-----------+
|  4 | Javiera | Marin    |   67 | 2024-11-15 16:02:48 | 2024-11-15 16:02:48 |         5 |
|  5 | Ricardo | Lopez    |   35 | 2024-11-15 16:02:48 | 2024-11-15 16:02:48 |         5 |
|  6 | Paola   | Reyes    |   21 | 2024-11-15 16:02:48 | 2024-11-15 16:02:48 |         5 |
+----+---------+----------+------+---------------------+---------------------+-----------+
```
## Crea 3 estudiantes que estén inscritos en el tercer curso:
```
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Rafael','Sanchez',17, 6);
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Castor','Timaure',22, 6);
insert into estudiantes (nombre, apellido, edad, curso_id ) values ('Anilec','Fuguet',15, 6);

select * from estudiantes where curso_id = 6;
+----+--------+----------+------+---------------------+---------------------+-----------+
| id | nombre | apellido | edad | created_at          | updated_at          | curso_id  |
+----+--------+----------+------+---------------------+---------------------+-----------+
|  7 | Rafael | Sanchez  |   17 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
|  8 | Castor | Timaure  |   22 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
|  9 | Anilec | Fuguet   |   15 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
+----+--------+----------+------+---------------------+---------------------+-----------+
```

## Recupera todos los estudiantes que estén inscritos en el primer curso:
select * from estudiantes where curso_id = 4;
+----+---------+----------+------+---------------------+---------------------+-----------+
| id | nombre  | apellido | edad | created_at          | updated_at          | curso_id  |
+----+---------+----------+------+---------------------+---------------------+-----------+
|  1 | Antonio | Perez    |   23 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
|  2 | Xavier  | Ruiz     |   40 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
|  3 | Pedro   | Colon    |   15 | 2024-11-15 15:58:31 | 2024-11-15 15:58:31 |         4 |
+----+---------+----------+------+---------------------+---------------------+-----------+

## Recupera todos los estudiantes que estén inscritos en el último curso:
```
select * from estudiantes
where curso_id = (select max(id) from cursos);
+----+--------+----------+------+---------------------+---------------------+-----------+
| id | nombre | apellido | edad | created_at          | updated_at          | curso_id  |
+----+--------+----------+------+---------------------+---------------------+-----------+
|  7 | Rafael | Sanchez  |   17 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
|  8 | Castor | Timaure  |   22 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
|  9 | Anilec | Fuguet   |   15 | 2024-11-15 16:06:15 | 2024-11-15 16:06:15 |         6 |
+----+--------+----------+------+---------------------+---------------------+-----------+
```

## Recupera el curso del último estudiante:
```
select * from cursos where id = (select curso_id from estudiantes where id = (select max(id) from estudiantes));
+----+---------+---------------------+---------------------+
| id | nombre  | created_at          | updated_at          |
+----+---------+---------------------+---------------------+
|  6 | Turismo | 2024-11-15 15:46:43 | 2024-11-15 15:46:43 |
+----+---------+---------------------+---------------------+
```

