-- 코드를 입력하세요
SELECT r.rest_id REST_ID, i.rest_name REST_NAME, i.food_type FOOD_TYPE, i.favorites FAVORITES, i.address ADDRESS, ROUND(AVG(r.review_score), 2) AS SCORE
from REST_REVIEW r
join REST_INFO i on i.rest_id = r.rest_id
where i.address like '서울%'
group by i.REST_ID
order by score desc, i.favorites desc;

