from collections import defaultdict

# 개인정보 n개
# 약관에 보관 휴요기간
def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_date = map(int, today.split('.'))
    term_dict = defaultdict(int)
    # terms 통해서 dictionary 생성
    for term in terms:
        kind, month = term.split()
        month = int(month)
        # 일수로 저장
        term_dict[kind] = month * 28
    
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        avail = term_dict[kind]
        date = list(map(int, date.split('.')))
        expire_year, expire_month, expire_date = date[0], date[1], date[2] + avail - 1
        while expire_date > 28:
            expire_month += 1
            expire_date -= 28
        while expire_month > 12:
            expire_year += 1
            expire_month -= 12
        # today와 비교
        # print(i+1)
        # print(expire_year, expire_month, expire_date)
        # print(today_year, today_month, today_date)
        # print()
        if today_year > expire_year:
            answer.append(i+1)
        elif today_year == expire_year:
            if today_month > expire_month:
                answer.append(i+1)
            elif today_month == expire_month:
                if today_date > expire_date:
                    answer.append(i+1)
        
    return answer