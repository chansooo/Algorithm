N = int(input())

final = 0
A = []
B = []
C = []
D = []
AB = dict()
for _ in range(N):
    a,b,c,d = map(int, input().split(" "))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(N):
    for j in range(N):
        temp = A[i] + B[j]
        if temp in AB:
            AB[temp] += 1
        else:
            AB[temp] = 1
for i in range(N):
    for j in range(N):
        temp = -(C[i] + D[j])
        if temp in AB :
            final += AB[temp]

print(final)