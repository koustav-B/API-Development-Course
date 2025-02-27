/*select* from products where id=1 or id=2 or id=3;

select* from products where id in(1,2,3); 
select* from products;*/
select* from products where name like 'mo%';
select* from products;
select* from products order by price;
select* from products order by price desc;
select* from products limit 5;
select* from products where price>10 limit 2;