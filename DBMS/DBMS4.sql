CREATE TABLE EMP(
empno numeric(4),
ename varchar(10),
designation varchar(10),
salary numeric(8,2)
);
select * from EMP;
ALTER TABLE EMP ALTER COLUMN empno TYPE numeric(6);

ALTER TABLE EMP ADD COLUMN qualification varchar(6);

ALTER TABLE EMP ADD COLUMN qualification varchar(6);

ALTER TABLE EMP ADD COLUMN dob DATE, ADD COLUMN doj DATE;

ALTER TABLE EMP DROP COLUMN doj;

ALTER TABLE EMP DROP COLUMN dob, DROP COLUMN qualification;

TRUNCATE TABLE EMP;

DROP TABLE EMP;