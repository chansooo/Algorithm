
from collections import deque

n = int(input())

q = deque()
q.append([n])
ans = []

while q:
    a = q.popleft()
    cur = a[0]
    
    if cur == 1:
        ans = a
        break
    if cur % 3 == 0:
        q.append([cur // 3] + a)
    if cur % 2 == 0:
        q.append([cur // 2] + a)
    q.append([cur-1] + a)
    
print(len(ans) - 1)
print(*ans[::-1])