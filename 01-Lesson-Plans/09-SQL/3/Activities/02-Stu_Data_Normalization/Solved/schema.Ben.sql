create table owners (
	id int ,
	name varchar
);
create table pets (
	id int,
	owner_id int,
	name varchar,
	pet_type_id int
);
create table pet_types (
	id int,
	name varchar,
	service_id int
);
create table service_types (
	id int,
	name varchar
);
INSERT INTO service_types(
	id, name)
	VALUES (1, 'walk'), (2,'Feed'), (3,'hop');
insert into pet_types (id, name, service_id)
values
(1,'dog',1),
(2, 'cat',2),
(3,'rabbit',3);
insert into owners (id, name)
values 
(1,'Sally'),
(2,'Charles'),
(3,'Angela'),
(4,'Kelly'),
(5,'Sam'),
(6,'Cassie');
insert into pets (id, name, owner_id, pet_type_id)
values
(1,'Zeus',1,1),
(2,'Kevin',2,1),
(3,'Sprinkles',3,2),
(4,'Jumper',4,2),
(5,'Hoppy',5,3),
(6,'Rex',6,1),
(7,'Fido',1,1),
(8,'Carrot',6,3);