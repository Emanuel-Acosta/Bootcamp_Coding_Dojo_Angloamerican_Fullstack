-- unir dos tablas relacionadas
select * from practica_joins.sitios
join clientes on cliente_id = clientes.id;

-- otra 
select * from practica_joins.prospectos
join sitios on sitio_id = sitios.id;

-- funciones tipo join
-- contar total de clientes
SELECT COUNT(id) as total_clientes FROM clientes;
-- promedio de montos de cobro()( tabla cobranza)
SELECT AVG(monto) as promedio FROM cobranza;
-- suma total de montos cobrados (tabla cobranza)
SELECT SUM(monto) as suma_total FROM cobranza; 
-- contar prospectos por sitio (prospectos)
SELECT sitio_id, COUNT(*) as total_prospectos FROM prospectos GROUP BY sitio_id;







