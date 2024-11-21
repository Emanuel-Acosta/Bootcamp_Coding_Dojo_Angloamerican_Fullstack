INSERT INTO productos (id, nombre) VALUES
(1, 'Laptop HP'),
(2, 'Monitor Dell'),
(3, 'Teclado Mecánico'),
(4, 'Mouse Gaming');
INSERT INTO categorias (id, nombre) VALUES
(1, 'Computadoras'),
(2, 'Periféricos'),
(3, 'Gaming'),
(4, 'Oficina');


-- Laptop HP -> Computadoras
-- Laptop HP -> Oficina
INSERT INTO productos_has_categorias (producto_id, categoria_id) VALUES
(1, 1), (1,4);
-- Monitor Dell -> Periféricos
-- Monitor Dell -> Oficina
INSERT INTO productos_has_categorias (producto_id, categoria_id) VALUES (2, 2),(2,4);
-- Teclado Mecánico -> Periféricos
-- Teclado Mecánico -> Gaming
INSERT INTO productos_has_categorias (producto_id, categoria_id) VALUES (3, 2), (3,3);
-- Mouse Gaming -> Periféricos
-- Mouse Gaming -> Gaming
INSERT INTO productos_has_categorias (producto_id, categoria_id) VALUES (4, 2), (4,3);

-- muchos a muchos join
SELECT * FROM categorias
JOIN productos_has_categorias ON categorias.id = categoria_id 
JOIN productos ON productos.id = producto_id;