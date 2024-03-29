select u.USER_ID, u.NICKNAME, sum(b.price) TOTAL_SALES
from used_goods_user u, used_goods_board b
where u.user_id = b.writer_id and b.status = "DONE"
group by u.user_id
having sum(b.price) >= 700000
order by sum(b.price) asc;





# SELECT u.user_id USER_ID, u.nickname NICKNAME, sum(b.price) TOTAL_SALES
# from used_goods_user u
# left join used_goods_board b
# on u.user_id = b.writer_id and b.status = 'DONE'
# group by u.user_id
# having TOTAL_SALES >= 700000
# order by TOTAL_SALES asc;