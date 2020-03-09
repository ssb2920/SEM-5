create table sales_order(
	order_no varchar(6),
	order_date date,
	client_no varchar(6),
	dely_addr varchar(25),
	salesman_no varchar(6),
	dely_type char(1),
	billed_yn char(1),
	dely_date date,
	order_status varchar(10)
);
insert into sales_order values('123', '2018-01-12','C001','Mumbai','20','p','y','2018-01-17','delivered');
insert into sales_order values('456', '2018-02-18','C002','Santacruz','21','c','n','2018-02-20','delivered');
insert into sales_order values('789', '2018-05-22','C003','Sanpada','22','p','y','2018-05-24','out for de');
insert into sales_order values('012', '2018-07-24','C004','Dongri','23','p','n','2018-07-27','shipping');
insert into sales_order values('345', '2018-09-26','C005','Pune','24','c','y','2018-09-30','ordplac');
insert into sales_order values('678', '2018-09-27','C001','Kalina','25','c','y','2018-11-30','ord plac');
select * from product_master;
select * from client_master where name like '_a%';
select * from client_master where city like '_a%';
select * from client_master where city='mumbai';
select * from client_master where bal_due>10000;
select * from sales_order where extract('month' from dely_date)=01;
select * from sales_order where client_no='C001' or client_no = 'C005';
select * from product_master where sell_price>200 and sell_price<=500;
select product_no,sell_price*1.5 as "new_price" from product_master where sell_price>150;
select count(*) from sales_order;
select avg(sell_price) from product_master;
select min(sell_price),max(sell_price) from product_master;
select count(*) from product_master where sell_price>250;


