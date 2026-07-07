CREATE DATABASE usuarios_db;
USE usuarios_db;

CREATE TABLE tipo_usuario(
id_tipo_usuario INT AUTO_INCREMENT  PRIMARY KEY,
descripcion_tipo_usuario VARCHAR(100),
created_at timestamp DEFAULT current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
created_by varchar(100),
update_by varchar(100),
deleted tinyint (1) default (0)
);

CREATE TABLE usuarios(
id_usuario INT AUTO_INCREMENT  PRIMARY KEY,
usuario VARCHAR(50) NOT NULL UNIQUE,
password_hash VARCHAR(100) NOT NULL,
fk_tipo_usuario INT NOT NULL,
created_at timestamp DEFAULT current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
created_by varchar(100),
update_by varchar(100),
deleted tinyint (1) default (0),
FOREIGN KEY (fk_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario)
);