Links: http://sqlfiddle.com
https://www.journaldev.com/sql

****************************************************************************************************************************************************************
#2016-1

CREATE TABLE envelope (id int, user_id int);
CREATE TABLE docs (idnum int, pageseq int, doctext varchar(100));

INSERT INTO envelope VALUES  (1,1),  (2,2),  (3,3);
INSERT INTO docs (idnum, pageseq) VALUES  (1,5),  (2,6),  (null,0);

UPDATE docs as d INNER JOIN envelope as e ON e.id=d.idnum SET d.doctext=e.user_id;

UPDATE docs as d INNER JOIN envelope as e ON e.id=d.idnum SET d.doctext=d.pageseq 
where exists (SELECT * FROM envelope as dd WHERE dd.id=e.id);
****************************************************************************************************************************************************************
#2016-2

CREATE TABLE Employee (employee varchar(10), salary decimal);

INSERT INTO Employee (employee, salary) VALUES  ('Emloyee01',500),  ('Emloyee02',550),  
('Emloyee03',450), ('Emloyee04',600), ('Emloyee05',650), ('Emloyee06',700), ('Emloyee07',750), 
('Emloyee08',400), ('Emloyee09',800), ('Emloyee10',350), ('Emloyee11',850);

#Option 1:
select * into Employee_result from Employee order by salary desc limit 10;

select * from Employee order by salary desc;

select * from Employee_result order by salary asc limit 1

#Option 2:
select * from (select * from Employee order by salary desc limit 10) as emp order by emp.salary asc limit 1
****************************************************************************************************************************************************************
#2016-3

CREATE TABLE users (id int);

INSERT INTO users (id) VALUES  (1),  (2),  
(3), (4), (5), (6), (7), 
(8), (9), (10), (11);

select id from users where id%2 = 1 limit 100
****************************************************************************************************************************************************************
#2017-1

CREATE TABLE students (id int, name varchar, marks int);
create table GRADES (grade int, min_mark int, max_mark int);

INSERT INTO students (id, name, marks) 
VALUES  (1,'Julia',88),  (2,'Samantha',68), (3,'Maria',99), (4,'Scarlet',78), 
(5,'Ashley',63), (6,'Jane',81);

insert into grades (grade, min_mark, max_mark)
values (1,0,9), (2,10,19), (3,20,29), (4,30,39), (5,40,49), (6,50,59), (7,60,69), (8,70,79), 
(9,80,89), (10,90,100);

select * into students_temp from students as s inner join grades as g on s.marks between g.min_mark and g.max_mark;

select * from students_temp;

update students_temp set name = 'Null' where grade < 8;

select name, grade, marks from students_temp order by marks desc;
****************************************************************************************************************************************************************
#2017-2

CREATE TABLE city (id int, name varchar(17), COUNTRYCODE varchar(3), DISTRICT varchar(2), POPULATION int);
create table country (code varchar(3), NAME varchar(44), CONTINENT varchar(13), REGION varchar(25), POPULATION int, CAPITAL varchar(4));

INSERT INTO city (id, name, COUNTRYCODE, DISTRICT, POPULATION) 
VALUES  (1,'Kiev','Ukr', 'NA', 550),  (2,'Berlin','Ger', 'NA', 400), (4,'London','UK', 'NA', 350), 
(5,'Sidney','Aus', 'NA', 600), (6,'Washington','USA', 'NA', 700), (7,'Lima','Per', 'NA', 200), 
(8,'Brisbon','Aus', 'NA', 330), (9,'Bristol','Aus', 'NA', 445);


insert into country (code, name, continent, region, population, capital)
values ('Ukr','Ukraine', 'Eurasia', 'Europe', 48000, 'Kiev'),
('Ger','Germany', 'Eurasia', 'Europe', 96000, 'Berl'),
('UK','United Kingdom', 'Eurasia', 'Europe', 75000, 'Lond'),
('Aus','Australia', 'Australia', 'Australia', 85000, 'Sidn'),
('USA','United States', 'North America', 'NA', 500000, 'Wash'),
('Per','Peru', 'Latin America', 'LA', 65000, 'Lima'),
('Jap','Japan', 'Eurasia', 'Asia', 95000, 'Toki'),
('Egy','Egypt', 'Africa', 'Africa', 70000, 'Cair');

select co.continent, ROUND(avg(ci.population)) from country as co 
inner join city as ci on ci.countrycode = co.code group by co.continent;
****************************************************************************************************************************************************************
#2018-1

CREATE TABLE customers (id int, name varchar);
create table orders (id int, customerid int);


INSERT INTO customers (id, name) 
VALUES  (1,'Joe'), (2,'Henry'), (3,'Sam'), (4,'Max');


insert into orders (id, customerid)
values (1,3), (2,1);

select * from customers as c inner join orders as o on o.customerid = c.id;

select * from customers where id not in(select c.id from customers as c inner join orders as o on o.customerid = c.id)
****************************************************************************************************************************************************************
#2018-2

CREATE TABLE logs (id int, num int);

INSERT INTO logs (id, num) 
VALUES  (1,1), (2,1), (3,1), (4,2), (5,1), (6,2), (7,2);

SELECT lc.num from logs as lc inner join logs as lp1 
on lp1.id=lc.id-1 
inner join logs as lp2
on lp2.id=lc.id-2
where lp1.num = lc.num
and lp2.num = lc.num