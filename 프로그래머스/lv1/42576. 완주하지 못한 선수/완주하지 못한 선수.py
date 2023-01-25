from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    for par in participant:
        dic[par] += 1
    for com in completion:
        dic[com] -= 1
    for people in dic:
        if dic[people] == 1:
            return people

    return ""