
from collections import deque

n, m = map(int, input().split())

q = deque()
q.append((n, 1))

while q:
    num, count = q.popleft()
    if num > m:
        continue
    if num == m:
        print(count)
        break
    q.append((num * 2, count + 1))
    q.append((int(str(num) + "1"), count + 1))
else:
    print(-1)

