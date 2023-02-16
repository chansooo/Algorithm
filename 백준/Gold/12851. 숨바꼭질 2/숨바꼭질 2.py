import sys
from collections import deque
input = sys.stdin.readline

a_location, b_location = map(int, input().split())
visited = [0] * 200001
q = deque()
q.append([a_location, 0])

min_time = float('inf')
ans_count = 1

while q:
    location, count = q.popleft()
    if count > min_time:
        continue

    if location == b_location:
        # 같은 count가 나왔을 떄 
        if min_time == count:
            ans_count += 1
        elif min_time > count:
            min_time = count
            ans_count = 1
            
    arr = [location - 1, location + 1, location * 2]

    for a in arr:
        if 0 <= a <= 200000 and (visited[a] == 0 or visited[a] == count + 1):
            visited[a] = count + 1
            q.append([a, count + 1])


print(min_time)
print(ans_count)