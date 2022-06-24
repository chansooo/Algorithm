
dx = [2, 2, -2, -2, 1, 1, -1 , -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

grid_y = ['q', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

A = input()
x = int(A[1])
y = str(grid_y).find(A[0])
print(y)
count =0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx < 1 or ny < 1 or nx > 8 or ny > 8):
        continue
    count += 1
    print(nx, ny)
    
print(count)