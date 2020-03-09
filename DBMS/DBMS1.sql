create table client_master(
	Client_no varchar(6),
	name varchar(20),
	address varchar(30),
	city varchar(15),
	pincode numeric(8),
	state varchar(15),
	Bal_due numeric(8,2)
);
create table product_master(
	product_no varchar(6),
	description varchar(15),
	profit_per numeric(4,2),
	unit_measure varchar(10),
	Qty_in_hand numeric(8),
	reorder_lvl numeric(8),
	sell_price numeric(8,2),
	cost_price numeric(8,2)
);
insert into client_master values('C001','Sherwin','Santacruz','Mumbai','400055','Maharashtra',15000);
insert into client_master values('C002','Sanfer','Andheri','Delhi','700057','Delhi',5000);
insert into client_master values('C003','Mayank','Kalina','Pune','406983','Maharashtra',9000);
insert into client_master values('C004','Princeton','Dongri','Bhyander','400069','Maharashtra',500);
insert into client_master values('C005','Carol','Sanpada','Chennai','675484','Tamilnadu',7950);
insert into client_master values('C006','Surya','M_Colony','Patna','541055','Bihar',15000);
insert into product_master values('567','hello',50,'unit',60,70,200,100);
insert into product_master values('890','world',60,'unit2',70,80,300,200);
insert into product_master values('678','hi',70,'unit3',80,90,400,300);
insert into product_master values('645','bye',80,'unit4',90,100,500,400);
insert into product_master values('876','goodbye',90,'unit5',100,110,600,500);

select name from client_master;
select * from client_master;
select name,city from client_master;
select * from product_master;
select name from client_master where city='Mumbai';
update client_master set city = 'mumbai' where Client_no='C001';
update client_master set Bal_due = 1000 where Client_no='C005';
update product_master set cost_price=560 where description='hi'
delete from product_master where Qty_in_hand<70;
delete from client_master where state='Tamilnadu';