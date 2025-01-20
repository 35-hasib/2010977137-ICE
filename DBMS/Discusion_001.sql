
-- 01
select * from sysobjects where xtype = 'U'

-- Task 01

select * from titles where ytd_sales > 8000

-- Task 02

select * from titles where royalty between 12 and 24

-- 03

select * from titles order by price desc

-- 04

select max(price) as max_price from titles
select min(price) as min_price from titles
select avg(price) as avg_price from titles

-- 05
select * from titles
select type, max(price) as max_price from titles group by type

select type, avg(price) as max_price from titles group by type having avg(price) > 14

-- Task 03
select avg(price) , sum(royalty) from titles

--07
select 'Name' = SUBSTRING(au_fname,1,1) + '.' + au_lname , phone from authors