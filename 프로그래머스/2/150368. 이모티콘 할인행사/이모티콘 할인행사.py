from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    avails = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    for avail in avails:
        user_number = 0
        all_cost = 0
        emoticon_real = [int((100 - discount) * emoticon / 100) for discount, emoticon in zip(avail, emoticons)]
        # 한 사람씩 확인
        for buy_percent, max_buy in users:
            # 사는 이모티콘 인덱스 저장
            buys = []
            for i in range(len(emoticons)):
                # print(avail[i], buy_percent)
                if avail[i] >= buy_percent:
                    buys.append(i)
            # 총 가격 확인
            cost = 0
            for i in buys:
                cost += emoticon_real[i]
                # print(emoticon_real[i])
            # print("avail", avail)
            # print("buys: ", buys)
            # print("cost: ", cost)
            # print("max buy, percent: ", max_buy, buy_percent)
            # print()
            # cost >= max_buy 이면 이모티콘 플러스 가입
            if cost >= max_buy:
                # all_cost += max_buy
                user_number += 1
            # 넘지 않으면 cost 더하기
            else:
                all_cost += cost
            
        # 경우의 수끼리 비교해서 user_number 가장 크게, 같다면 all_cost 가장 크게
        if answer[0] < user_number:
            answer[0] = user_number
            answer[1] = all_cost
        elif answer[0] == user_number and answer[1] < all_cost:
            answer[0] = user_number
            answer[1] = all_cost
            
    # 각 사라
    return answer