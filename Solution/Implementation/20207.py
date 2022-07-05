result = 0
N = int(input())
todo = [0 for _ in range(366)]
for _ in range(N):
    start, finish = map(int, input().split())
    for i in range(start, finish+1):
        todo[i] += 1

max = 0
length = 0
for i in range(366):
    if todo[i] == 0:
        result += max*length
        max =0
        length =0
        continue
    if todo[i] > max:
        max = todo[i]
    length += 1
    

print(result)
    