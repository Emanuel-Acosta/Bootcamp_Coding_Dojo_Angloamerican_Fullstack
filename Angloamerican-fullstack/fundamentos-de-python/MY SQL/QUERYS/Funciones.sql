select * from x.tweets;

-- calcular el largo de un tweets
select length(tweet) from x.tweets
where id = 2;

-- calcular el largo de todos los tweets
select id , length(tweet) from x.tweets;

-- retornar un tweet en mayuscula
select id , upper(tweet) from x.tweets
where id = 4;

-- retornar 3 tweets en minuscula
select id , lower(tweet) from x.tweets
 limit 1,3;
 
 -- el minuto del primer tweet
 select id, tweet, year(created_at) from x.tweets
 where id =1;
 
 -- mostrar nombre completo de todos los usuarios 
 select id, concat(nombre,' ',apellido) as nombre_completo from x.usuarios;
 
 -- calcular edad usuario restan NOW() 
 select nombre, fecha_nacimiento, datediff(now(), fecha_nacimiento)/365.2425 as edad_aprox from x.usuarios;
 
 -- if(): clasificar tweets por longitud(amyor a 100 caracter => tweet largo)
 select tweet, if(length(tweet)>100, 'largo', 'corto') as clasificacion from x.tweets
 
 
 
 
 
 
 
 
 
 
 

