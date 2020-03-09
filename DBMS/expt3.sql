create table client_master(
clientno varchar(6),
name varchar(20),
address varchar(30),
city varchar(15),
pincode numeric(8),
state varchar(15),
balance numeric(10,2)
)
create table Product_master(
product_no varchar(6),
description varchar(15),
Profit_percent numeric(4,2),
Unit_measure varchar(10),
Qty_on_hand numeric(8),
Reorder_level numeric(8),
Sell_price numeric(8,2),
Cost_price numeric(8,2)
)

insert into client_master values('123','abc','cba','a',10,'b',100)
insert into client_master values('456','def','fed','c',20,'d',200)
insert into client_master values('789','ghi','ihg','e',30,'f',300)
insert into client_master values('012','jkl','lkj','g',40,'h',400)
insert into client_master values('345','mno','onm','i',50,'j',500)
insert into client_master values('345','mno','onm','mumbai',50,'j',500)

insert into Product_master values('567','hello',50,'unit',60,70,200,100)
insert into Product_master values('890','world',60,'unit2',70,80,300,200)
insert into Product_master values('678','hi',70,'unit3',80,90,400,300)
insert into Product_master values('645','bye',80,'unit4',90,100,500,400)
insert into Product_master values('876','goodbye',90,'unit5',100,110,600,500)

select name from client_master
select * from client_master
select name,city from client_master
select * from Product_master
select * from client_master where city='mumbai'
update client_master set city='mumbai' where clientno='456'
update client_master set balance=1000 where clientno='456'
update Product_master set Cost_price=560 where description='hi'
delete from Product_master where Qty_on_hand<70
delete from client_master where state='d'

select * from client_master
select * from Product_master
