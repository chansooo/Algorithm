import py_compile

T = int(input())

for _ in range(T):
    N = int(input())
    list1 = list(map(int, input().split()))
    print(min(list1), max(list1))