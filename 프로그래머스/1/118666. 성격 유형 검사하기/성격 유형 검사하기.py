from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    dic = defaultdict(int)

    for s, c in zip(survey, choices):
        if c > 4:
            dic[s[0]] += (4 - c)
        elif c == 4:
            continue
        else:
            dic[s[1]] += (c - 4)
    
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
    # print(dic)
    
    return answer