select i.REST_ID, i.REST_NAME ,i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, ROUND(AVG(r.review_score), 2) score
from rest_info i, rest_review r
where i.rest_id = r.rest_id and
    i.address like '서울%'
group by i.rest_id
order by score desc, i.favorites desc;




# -- 코드를 입력하세요
# SELECT r.rest_id REST_ID, i.rest_name REST_NAME, i.food_type FOOD_TYPE, i.favorites FAVORITES, i.address ADDRESS, ROUND(AVG(r.review_score), 2) AS SCORE
# from REST_REVIEW r
# join REST_INFO i on i.rest_id = r.rest_id
# where i.address like '서울%'
# group by i.REST_ID
# order by score desc, i.favorites desc;