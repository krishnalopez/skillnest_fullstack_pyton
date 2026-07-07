use usuarios_db;
insert into tipo_usuario(descripcion_tipo_usuario, created_by, update_by)
values ('Empleado', 'system', 'system'),
       ('Supervisor', 'system', 'system');
insert into usuarios(usuario, password_hash, fk_tipo_usuario, created_by, update_by)
values ('juan','juan123', 1 ,'system','system'),
       ('martin','nunez23', 1 ,'system','system'),
       ('maria','mariaxx', 1 ,'system','system'),
       ('admin','admin123', 2 ,'system','system');