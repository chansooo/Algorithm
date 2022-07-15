
# 서류, 면접 둘 중 하나라도 1등

import sys

T = int(input()) #테스트케이스

for i in range(T):
    count = 1
    people = []
    
    N = int(input())
    for i in range(N):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper, interview])

    people.sort() # 서류 기준 오름차순 정렬
    max_ = people[0][1]
    
    for i in range(1,N):
        if max_ > people[i][1]:
            count += 1
            max_ = people[i][1]

    print(count)