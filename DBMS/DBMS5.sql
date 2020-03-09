create table company1(
	id int ,
	name text not null,
	age int not null,
	address varchar(50),
	salary real
	
);
select * from company1;
insert into company1 values(01,NULL,NULL,'LA',250000);
create table company3(
	id int not null ,
	name text,
	age int unique,
	address varchar(50),
	salary real
);
insert into company3 values(02,'CAJE',25,'NY',50000);
insert into company3 values(02,'CAJE',25,'NY',50000);
create table company4(
	id int primary key,
	name text ,
	age int ,
	address varchar(50),
	salary real
)
insert into company4 values(03,'LOGAN',11,'CHICAGO',40000);
insert into company4 values(03,'LOGAN',11,'CHICAGO',40000);
create table employee(
	id  int primary key,
	name text,
	age int ,
	address varchar(50),
	salary real	
);
create table department(
	id int primary key,
	name varchar(50) not null,
	empid int references employee(id)
);
insert into employee values(1,'JAKE',11,'CHICAGO',40000);
insert into employee values(2,'SENSEI',11,'US',40000);
select * from employee;
insert into department values(07,'AJ STYLES',1);
insert into department values(08,'JOHN',2);
select * from department;
create table company5(
	id int,
	name text,
	age int,
	address varchar(50),
	salary real check(salary>0)
);
insert into company5 values(09,'BAREN',24,'MADH',-1);









