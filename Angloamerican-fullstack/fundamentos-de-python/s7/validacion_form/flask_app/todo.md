## TO DO
- [x ]  Mostrar usuarios que no esten en el viaje solamente `linea 77` `flask_app\controllers\viajes.py`
- [ ]  Eliminar usuarios del viaje 
eliminar participantes antes de eliminar un viaje

ALTER TABLE participantes_viaje DROP FOREIGN KEY participantes_viaje_ibfk_1;
ALTER TABLE participantes_viaje ADD CONSTRAINT participantes_viaje_ibfk_1 FOREIGN KEY (id_viaje) REFERENCES viajes (id_viaje) ON DELETE CASCADE;