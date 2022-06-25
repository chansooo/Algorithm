N = int(input())

total = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
stu = [] # 학생들 배열
feel = [[0 for i in range(N)] for j in range(N)]
arr = [[0 for i in range(N)] for j in range(N)]
save = [[] for i in range(N**2+1)] # 학생들 관계 배열(누가 누구 좋아하는지)

# 입력 처리
for i in range(N**2):
    a = list(map(int, input().split()))
    stu.append(a)
    save[a[0]].append(a[1:])

# 친구들을 자리에 앉혀봐요
for i in range(N**2):
    temp = []
    for x in range(N):
        for y in range(N):
            # 누가 앉아있는 경우
            if arr[x][y] != 0: 
                continue
            like = 0
            empty = 0
            for z in range(4):
                dx = x + nx[z]
                dy = y + ny[z]
                # 경기장 밖에서 사망
                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue
                # 1번째 조건
                #  i번째 학생의 좋아하는 사람들 중에 지금 보고있는 좌표에 있는 사람이 있다면
                if arr[dx][dy] in stu[i][1:]:
                    # 현재 보는 자리가 좋아하는 사람 옆이니까 like 올려줘
                    like += 1 
                # 2번째 조건
                # 근데 자리가 비었다면?
                if arr[dx][dy] == 0:
                    # empty 를 올려줘
                    empty += 1
            # 튜플을 temp에 저장
            temp.append((like, empty, (x, y)))
    # 저장된 temp 배열을 like, empty는 내림차순, x,y는 오름차순으로 정렬
    temp.sort(key = lambda x: (-x[0], -x[1], x[2]))
    # 우선순위 가장 높은 자리의 좌표에 현재 학생을 앉힌다
    arr[temp[0][2][0]][temp[0][2][1]] = stu[i][0]

# 만족도 조사
for i in range(N):
    for j in range(N):
        # 현재 좋아하는 친구가 근처에 있는지 확인해야하는 친구
        now = arr[i][j]
        near = 0
        # 어떤 친구의 상하좌우에 좋아하는 친구가 있다면,,,, 해당 자리의 feel을 올려준다...
        for z in range(4):
            dx = i + nx[z]
            dy = j + ny[z]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            # 지금 보고 있는 자리에 앉아있는 애가 내가 좋아하는 애 중 한 명이라면?
            if arr[dx][dy] in save[now][0]:
                near += 1
        feel[i][j] = near
        
# 계산한 feel 배열 값 정리
for i in range(N):
    for j in range(N):
        if feel[i][j] == 1:
            total += 1
        elif feel[i][j] == 2:
            total += 10
        elif feel[i][j] == 3:
            total += 100
        elif feel[i][j] == 4:
            total += 1000
            
print(total)