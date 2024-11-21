# core paises

## 1¿Qué consulta ejecutarías para obtener todos los países que hablan español? Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. 
```
select 
paises.nombre , idiomas.idioma, idiomas.porcentage
from idiomas
join paises on idiomas.pais_id = paises.id
where idiomas.idioma = 'Español'
order by idiomas.porcentage desc; 
```

## 2¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país, el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente.

```
SELECT paises.nombre, idiomas.idioma, COUNT(ciudades.id) AS numero_ciudades
FROM paises
JOIN idiomas ON paises.id = idiomas.pais_id
JOIN ciudades ON paises.id = ciudades.pais_id
GROUP BY paises.nombre, idiomas.idioma
ORDER BY numero_ciudades DESC;
```

## 3¿Qué consulta ejecutarías para obtener todos ciudades de Chile con una población mayor a 200,000? Tu consulta debe ordenar el resultado por población en orden descendente.
```
select ciudades.nombre, ciudades.distrito, ciudades.poblacion
from ciudades
join paises on ciudades.pais_id = paises.id
where paises.nombre = 'Chile' and ciudades.poblacion > 200000
order by ciudades.poblacion desc;

+-------------------+---------------+-----------+
| nombre            | distrito      | poblacion |
+-------------------+---------------+-----------+
| Santiago de Chile | Santiago      |   4703954 |
| Puente Alto       | Santiago      |    386236 |
| ViÃ±a del Mar     | ValparaÃ­so   |    312493 |
| ValparaÃ­so       | ValparaÃ­so   |    293800 |
| Talcahuano        | BÃ­obÃ­o      |    277752 |
| Antofagasta       | Antofagasta   |    251429 |
| San Bernardo      | Santiago      |    241910 |
| Temuco            | La AraucanÃ­a |    233041 |
| ConcepciÃ³n       | BÃ­obÃ­o      |    217664 |
| Rancagua          | OÂ´Higgins    |    212977 |
+-------------------+---------------+-----------+
```

## 4¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%? Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. 
```
select paises.nombre, idiomas.idioma, idiomas.porcentage
from idiomas
join paises on idiomas.pais_id = paises.id
where idiomas.porcentage > 89
order by idiomas.porcentage desc;
```

## 5¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000?
```
select paises.nombre, paises.area_superficie, paises.poblacion
from paises
where paises.area_superficie < 501 and paises.poblacion > 100000;

+----------------------------------+-----------------+-----------+
| nombre                           | area_superficie | poblacion |
+----------------------------------+-----------------+-----------+
| Aruba                            |          193.00 |    103000 |
| Barbados                         |          430.00 |    270000 |
| Macao                            |           18.00 |    473000 |
| Maldives                         |          298.00 |    286000 |
| Malta                            |          316.00 |    380200 |
| Mayotte                          |          373.00 |    149000 |
| Saint Vincent and the Grenadines |          388.00 |    114000 |
+----------------------------------+-----------------+-----------+

```
## 6¿Qué consulta ejecutarías para obtener países en el que el tipo de gobierno es República, un capital superior a 2000 y una esperanza de vida mayor a 78 años? 
```
select paises.nombre, paises.tipo_gobierno, paises.capital, paises.esperanza_vida
from paises
where paises.tipo_gobierno = 'República' and paises.capital > 2000 and paises.esperanza_vida = 78;
```

## 7¿Qué consulta ejecutarías para obtener todas las ciudades de Colombia dentro del distrito de Valle con una población mayor a 200,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población. 
```
select paises.nombre, ciudades.nombre, ciudades.distrito, ciudades.poblacion
from ciudades
join paises on ciudades.pais_id = paises.id
where paises.nombre = 'Colombia' and ciudades.distrito = 'Valle' and ciudades.poblacion > 200000;

+----------+--------------+----------+-----------+
| nombre   | nombre       | distrito | poblacion |
+----------+--------------+----------+-----------+
| Colombia | Cali         | Valle    |   2077386 |
| Colombia | Palmira      | Valle    |    226509 |
| Colombia | Buenaventura | Valle    |    224336 |
+----------+--------------+----------+-----------+
```

## 8¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y el número de países. Además, debe ordenar el resultado por el número de países en orden descendente.

```
select region, count(paises.id) as numero_paises
from paises
group by region
order by numero_paises desc;

+---------------------------+---------------+
| Caribe                    |            24 |
| África Oriental           |            20 |
| Medio Oriente             |            18 |
| África Occidental         |            17 |
| Europa del Sur            |            15 |
| Asia Sur y Central        |            14 |
| Sudamérica                |            14 |
| Sureste de Asia           |            11 |
| Polinesia                 |            10 |
| Europa del Este           |            10 |
| Africa Central            |             9 |
| Europa Occidental         |             9 |
| Central America           |             8 |
| Asia Oriental             |             8 |
| Países Nórdicos           |             7 |
| Africa del Norte          |             7 |
| Micronesia                |             7 |
| Antarctica                |             5 |
| Australia y Nueva Zelanda |             5 |
| Norte América             |             5 |
| África Austral            |             5 |
| Melanesia                 |             5 |
| Países Bálticos           |             3 |
| Islas Británicas          |             2 |
| Micronesia/Caribe         |             1 |
+---------------------------+---------------+
```