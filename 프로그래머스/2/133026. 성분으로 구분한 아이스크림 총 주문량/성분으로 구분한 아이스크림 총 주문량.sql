select i.INGREDIENT_TYPE, sum(f.total_order) TOTAL_ORDER
from icecream_info i
left join first_half f on i.flavor = f.flavor
group by i.ingredient_type
order by TOTAL_ORDER asc;




















# SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) TOTAL_ORDER
# from first_half f
# left join icecream_info i on f.flavor = i.flavor
# group by i.ingredient_type
# order by TOTAL_ORDER asc;