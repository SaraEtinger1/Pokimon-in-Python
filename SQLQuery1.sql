--CREATE DATABASE py_database;

CREATE TABLE Pokemon 
	(pok_id int PRIMARY KEY,
	pok_name varchar(15),
	pok_type varchar(18),
	pok_height int,
	pok_weight int,
	)

	
create TABLE ownedby 
	(own_id int PRIMARY KEY,
	own_name varchar(15) ,
	own_type varchar(18),
	)
drop table ownedby


CREATE TABLE trainers(
	pok_id int foreign key REFERENCES pokemon (pok_id),
	own_id int foreign key REFERENCES ownedby (own_id),
	PRIMARY KEY(pok_id,own_id)
	)
