
square1 = []

square2 = []

square = [[] for _ in range(2)]

x1, y1, x2, y2 = map(int, input().split())
square[0].append([x1,y1])
square[0].append([x2, y2])
square[0].append([x1, y2])
square[0].append([x2,y1])


x3, y3, x4, y4 = map(int, input().split())
square[1].append([x3,y3])
square[1].append([x4, y4])
square[1].append([x3, y4])
square[1].append([x4,y3])

# 한 점 이상이 다른 사각형 안에 있다 -> face
# 한 점이 만난다 -> point
# 한 점과 다른 점의 



flag = False

for x, y in square[0]:
    # 한 점이 다른 사각형 아예 안에 있을 경우
    if x3 < x < x4 and y3 < y < y4:
        print("FACE")
        flag = True
        break
    elif x3 <= x1  and x2 <= x4 and y2 >= y4 and  y1 <= y3:
        print("FACE")
        flag = True
        break
    # 한 점의 x값이 다른 사각형과 같고 y 값이 그 사이
    elif  (x == x3 or x == x4) and y3 < y < y4 or (y == y3 or y == y4) and x3 < x < x4 :
        print("LINE")
        flag = True
        break
    elif (x == x3 or x == x4) and (y == y3 or y == y4):
        print("POINT")
        flag = True
        break

for x, y in square[1]:
    if flag:
        break
    # 한 점이 다른 사각형 아예 안에 있을 경우
    if x1 < x < x2 and y1 < y < y2:
        print("FACE")
        flag = True
        break
    elif y3 <= y1  and y2 <= y4 and x2 >= x4 and  x1 <= x3:
        print("FACE")
        flag = True
        break
    # 한 점의 x값이 다른 사각형과 같고 y 값이 그 사이
    elif  (x == x1 or x == x2) and y1 < y < y2 or (y == y1 or y == y2) and x1 < x < x2 :
        print("LINE")
        flag = True
        break
    elif (x == x1 or x == x2) and (y == y1 or y == y2):
        print("POINT")
        flag = True
        break


if not flag:
    print("NULL")