from collections import deque


S = input()
length = len(S)
flag = False
result = deque()
temp = deque()

for i in range(length):
    temp.append(S[i])
    #print(S[i])
    if S[i] == '<':
        if len(temp) != 0:
            temp.pop()
            for _ in range(len(temp)):
                result.append(temp.pop())
            temp.append('<')
        flag = True
        continue
    if S[i] == '>':
        flag = False
        for _ in range(len(temp)):
            result.append(temp.popleft())
        temp.clear()
        continue
    if flag == False and S[i] == ' ':
        temp.pop()
        for _ in range(len(temp)):
            result.append(temp.pop())
        result.append(' ')
    #print(temp)
        
if len(temp) != 0:
    if flag:
        for _ in range(len(temp)):
            result.append(temp.popleft())
    else:
        for _ in range(len(temp)):
            result.append(temp.pop())

print(''.join(result))

#print(*result)

