def solution(arr):
    num_set = []
    temp = -1
    for i in arr:
        if i == temp:
            continue
        else:
            temp = i
            num_set.append(i)
    return num_set