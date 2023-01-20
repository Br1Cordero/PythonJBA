
create database RedSocial;

use RedSocial;

create table tb_cliente(
Id int not null auto_increment,
Apellidos varchar (250),
Nombres varchar(250),
Genero varchar (1),
Email varchar (250),
Password varchar(250),
F_Creacion datetime default CURRENT_TIMESTAMP,
F_Modificacion datetime default '0000-00-00',
F_Eliminacion datetime default '0000-00-00',
primary Key (Id)
);

create table tb_publicacion_cuerpo(
Id int not null auto_increment,
Titulo varchar (50),
Contenido varchar (2000),
F_Creacion datetime default CURRENT_TIMESTAMP,
F_Modificacion datetime default '0000-00-00',
F_Eliminacion datetime default '0000-00-00',
primary key (Id)
);

create table tb_publicacion(
Id int not null auto_increment,
Usuario int not null,
Publicacion int not null,
F_Creacion datetime default CURRENT_TIMESTAMP,
F_Modificacion datetime default '0000-00-00',
F_Eliminacion datetime default '0000-00-00',
primary Key (Id),
FOREIGN Key (Usuario) references tb_cliente(Id),
foreign key (Publicacion) references tb_publicacion_cuerpo(Id)
);


DROP procedure IF EXISTS `InsertPublicacion`;

DELIMITER $$
USE `redsocial`$$
CREATE PROCEDURE InsertPublicacion (
In _Usuario int,
In _Titulo varchar (50),
In _Contenido varchar(2000)
)
BEGIN
	declare _Id int;
	INSERT INTO tb_publicacion_cuerpo (Titulo, Contenido) VALUES (_Titulo, _Contenido);
	set _Id = ( SELECT MAX(id) AS id FROM tb_publicacion_cuerpo);
    INSERT INTO tb_publicacion (Usuario, Publicacion) VALUES (_Usuario, _Id);
END$$



 -- drop database RedSocial;