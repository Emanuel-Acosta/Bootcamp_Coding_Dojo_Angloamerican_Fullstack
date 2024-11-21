
-- practica de left join
-- todos los tweets del usuario id = 2
SELECT * FROM usuarios
LEFT JOIN tweets ON usuarios.id = usuario_id
WHERE usuarios.id = 2;

-- si quisieramos solamente obtener los tweets hariamos esta consulta
SELECT tweet FROM usuarios
LEFT JOIN tweets ON usuarios.id = usuario_id
WHERE usuarios.id = 2;

-- ¿Y si queremos cambiar a que el resultado tenga como nombre de columna algo distinto? ¡Lo podemos hacer también!
SELECT tweet as tweets_de_vince FROM usuarios
LEFT JOIN tweets ON usuarios.id = usuario_id
WHERE usuarios.id = 2;

-- Qué consulta ejecutaremos para obtener todos los tweets que el usuario con id 1 ha marcado como favoritos?
SELECT nombre, tweet FROM usuarios
LEFT JOIN favoritos ON usuarios.id = favoritos.usuario_id
LEFT JOIN tweets ON favoritos.tweet_id = tweets.id
WHERE usuarios.id = 1;
#El primer LEFT JOIN une usuarios con favoritos
#El segundo LEFT JOIN une favoritos con tweets

-- Qué consulta ejecutaremos para obtener todos los tweets que el usuario con id 1 o el usuario con id 2ha marcado como favoritos?
SELECT nombre, tweet FROM usuarios
LEFT JOIN favoritos ON usuarios.id = favoritos.usuario_id
LEFT JOIN tweets ON favoritos.tweet_id = tweets.id
WHERE usuarios.id = 1 OR usuarios.id = 2;

-- 4. ¿Qué consulta ejecutaremos para obtener todos los seguidores del usuario con id 3?
SELECT usuarios.nombre as usuario, usuarios2.nombre as seguidor
FROM usuarios
LEFT JOIN seguidores ON usuarios.id = seguidores.usuario_id
LEFT JOIN usuarios as usuarios2 ON usuarios2.id = seguidores.seguidor_id
WHERE usuarios.id = 3;
#El primer LEFT JOIN une usuarios con seguidores
#El segundo LEFT JOIN une seguidores con usuarios, creando un alias usuarios2
#dándonos los usuarios que siguen a la tabla original

-- ¿Qué consulta ejecutaremos para obtener todos los usuarios que NO siguen al usuario con id 3?
SELECT *
FROM usuarios
WHERE usuarios.id NOT IN (
SELECT seguidor_id
FROM seguidores
WHERE usuario_id = 3
) AND usuarios.id != 3;

-- Por ejemplo, el siguiente query me regresará todos los nombres de usuarios y los tweets que han generado.
-- A pesar de que Rajon aún no tiene ningún tweet asociado, incluye su registro en el resultado.
SELECT nombre, tweet
FROM usuarios
LEFT JOIN tweets ON usuarios.id = tweets.usuario_id;

-- Si cambiáramos LEFT JOIN por un JOIN, el resultado sería distinto:
SELECT nombre, tweet
FROM usuarios
JOIN tweets ON usuarios.id = tweets.usuario_id;

