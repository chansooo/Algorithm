from itertools import combinations

n, m = map(int, input().split())
ret = list(combinations(range(1,n+1), m))
for r in ret:
    for i in r:
        print(i, end=' ')
    print()
