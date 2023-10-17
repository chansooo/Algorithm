SELECT book.CATEGORY, sum(TOTAL_SALES) TOTAL_SALES
from book
left join 
(select book_id, sum(sales) total_sales
from book_sales
where sales_date like '2022-01%'
group by book_id) a
on book.book_id = a.book_id
group by book.category
order by category asc