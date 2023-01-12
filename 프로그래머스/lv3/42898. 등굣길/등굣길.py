def solution(m, n, puddles):
    answer = 0
    map_ = [[0] * (m+1) for _ in range(n+1)]
    map_[0][1] = 1
    # 웅덩이는 -1로 세팅
    for x, y in puddles:
        map_[y][x] = -1
    for x in range(1, m+1):
        for y in range(1, n+1):
            if map_[y][x] == -1:
                map_[y][x] = 0
                continue
            up, left = map_[y-1][x], map_[y][x-1]
            map_[y][x] = (up + left) % 1000000007
            # print(map_)
    return map_[n][m]