from collections import defaultdict


N = int(input())
group = []
count = [0 for _ in range(N)]
for _ in range(N):
    weight, height = map(int, input().split())
    group.append([weight, height])


for index, cur in enumerate(group):
    cur_w, cur_h = cur
    for com_w, com_h in group:
        if cur_w < com_w and cur_h < com_h:
            count[index] += 1


for i in range(N):
    count[i] +=1
    
s = ' '.join(str(x) for x in count)
print(s)