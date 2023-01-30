
n, m = map(int, input().split())

ans = []

def dfs(count, index):
    if count - 1 == m:
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(index, n+1):
        ans.append(i)
        dfs(count+1, i)
        ans.pop()

dfs(1,1)