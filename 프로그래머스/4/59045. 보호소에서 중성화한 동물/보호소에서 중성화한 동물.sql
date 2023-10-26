-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins i, animal_outs o
where i.animal_id = o.animal_id and
    i.sex_upon_intake like "Intact%" and
    o.sex_upon_outcome not like "Intact%" 
    
