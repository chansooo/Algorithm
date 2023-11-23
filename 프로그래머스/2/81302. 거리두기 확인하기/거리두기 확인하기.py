def solution(places):
    answer = []

    
    # p가 나오면 +2씩 해서 확인해봐야 함
    for place in places:
        answer.append(check(place))

    return answer

def check(place):
    dir1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir2 = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    dir3 = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    for r in range(5):
        for c in range(5):
            if place[r][c] != 'P':
                continue
            # p가 나왔을 때 확인
            # 상하좌우에 사람 있을 경우 -> return 0
            for dr, dc in dir1:
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc):
                    continue
                if place[nr][nc] == 'P':
                    return 0
            for dr, dc in dir3:
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc):
                    continue
                if place[nr][nc] == 'P' and place[nr-dr//2][nc-dc//2] != 'X':
                    return 0
            for i in range(4):
                dr, dc = dir2[i]
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc):
                    continue
                if place[nr][nc] == 'P':
                    if place[r+dr][c] != 'X' or place[r][c+dc] != 'X':
                        return 0
                    
    return 1

def in_range(r, c):
    return 0 <= r and r < 5 and 0 <= c and c < 5