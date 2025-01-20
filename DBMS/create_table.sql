create table test001(
	student_id varchar(10) primary key,
	name varchar(20) not null,
	age int not null,
	relation_status varchar(20)
)

insert into test001 values
('2010977137', 'Hasib', 23, 'Single'),
('2011077117', 'Abir', 24, 'In a relation'),
('2010177123', 'Tarik', 22, 'In a relation'),
('2010277155', 'Touhid', 22, 'Mingle');

select * from test001