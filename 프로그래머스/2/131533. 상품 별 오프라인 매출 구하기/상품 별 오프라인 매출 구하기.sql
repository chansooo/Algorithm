-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.price * off.sales_amount) SALES
from product p, offline_sale off
where p.product_id = off.product_id
group by p.product_code
order by sales desc, p.product_code asc;