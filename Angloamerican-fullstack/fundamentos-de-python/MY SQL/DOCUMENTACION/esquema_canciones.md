## Crea 5 usuarios nuevos
```
insert into usuarios(nombre, email, contrasena)
 values
 ('User1','user1@gmail.com','1234')
,('User2','user2@gmail.com','5678')
,('User3','user3@gmail.com','9123')
,('User4','user4@gmail.com','3456')
,('User5','user5@gmail.com','7891');
```

## Crea 5 canciones (¡usa los datos de tus canciones favoritas!) nuevas
```
insert into canciones(titulo,artista) 
values 
 ('Like Stone', 'Audioslave')
,('Caney', 'Rawayana')
,('Nice to know you', 'Incubus')
,('Nookie', 'Limp Bizkit')
,('De la vida como pelicula', 'Cancerbero');
```

## Cambia el nombre del tercer usuario a Miyagi
```
update usuarios set nombre = 'Miyagi' where id= 3;
```
## Cambia el nombre de la primera canción a Macarena:
```
update canciones set titulo = 'Macarena' where id= 1;
```
## Haz que el primer usuario marque como favoritas las 3 primeras canciones
```
insert into favoritos(usuario_id, cancion_id) values(1,1),(1,2),(1,3);
```
## Haz que el segundo usuario marque como favoritas las 2 primeras canciones
insert into favoritos(usuario_id, cancion_id) values(2,1),(2,2);


