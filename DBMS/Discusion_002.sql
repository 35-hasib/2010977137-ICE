-- 01
select * from publishers
select * from authors
select * from titleauthor
select * from titles

select au_lname, title_id from titleauthor join authors on titleauthor.au_id = authors.au_id

-- task 01
--i
select au_lname, title from authors join titleauthor on authors.au_id = titleauthor.au_id join titles on titles.title_id = titleauthor.title_id
--ii
select au_lname, title,pub_name from authors join titleauthor on authors.au_id = titleauthor.au_id join titles on titles.title_id = titleauthor.title_id join publishers on publishers.pub_id = titles.pub_id

-- 02
select au_lname, pub_name from authors,publishers

-- task 02
select au_lname,pub_name,authors.city from authors join publishers on authors.city = publishers.city

-- 03 
select * from titles where royalty = (select avg(royalty)  from titles)

-- Task 03

select au_lname, royalty 
from authors join titleauthor on authors.au_id = titleauthor.au_id join titles on titles.title_id = titleauthor.title_id
where royalty = (select max(royalty) from titles)
 