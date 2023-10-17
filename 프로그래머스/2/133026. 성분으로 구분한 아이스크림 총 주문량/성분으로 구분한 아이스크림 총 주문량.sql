SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) TOTAL_ORDER
from first_half f
left join icecream_info i on f.flavor = i.flavor
group by i.ingredient_type
order by TOTAL_ORDER asc;