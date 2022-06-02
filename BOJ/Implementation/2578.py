
from operator import truediv


bingo_map = [list(map(int, input().split())) for _ in range(5)]
order = [list(map(int, input().split())) for _ in range(5)]
order_count = 0
def check_number(number):
    for i in range(5):
        for j in range(5):
            if bingo_map[i][j] == number:
                bingo_map[i][j] = 0

def check_bingo():
    bingo_count = 0
    for i in range(5):
        if bingo_map[i][0] == 0 and bingo_map[i][1] == 0 and bingo_map[i][2] == 0 and bingo_map[i][3] == 0 and bingo_map[i][4] == 0:
            bingo_count += 1
        if bingo_map[0][i] == 0 and bingo_map[1][i] == 0 and bingo_map[2][i] == 0 and bingo_map[3][i] == 0 and bingo_map[4][i] == 0:
            bingo_count += 1
    if bingo_map[0][0] == 0 and bingo_map[1][1] == 0 and bingo_map[2][2] == 0 and bingo_map[3][3] == 0 and bingo_map[4][4] == 0:
        bingo_count += 1
    if bingo_map[0][4] == 0 and bingo_map[1][3] == 0 and bingo_map[2][2] == 0 and bingo_map[3][1] == 0 and bingo_map[4][0] == 0:
        bingo_count += 1
    if bingo_count >= 3:
        return True
    return False

for i in range(5):
    for j in range(5):
        check_number(order[i][j])
        order_count += 1
        if check_bingo():
            print(order_count)
            quit()