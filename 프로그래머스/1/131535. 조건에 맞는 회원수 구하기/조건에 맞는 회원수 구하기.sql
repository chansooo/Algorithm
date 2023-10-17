-- 코드를 입력하세요
SELECT count(*) USERS
from user_info
where 
    age < 30 and
    age > 19 and
    joined like '2021%'
    