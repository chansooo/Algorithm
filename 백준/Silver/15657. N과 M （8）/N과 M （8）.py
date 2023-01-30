
n, m = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
ans = []

def dfs(count, index):
    if count -1 == m:
        print(' '.join(map(str, ans)))
        return 
    for i in range(index, n):
        ans.append(num_list[i])
        dfs(count+1, i)
        ans.pop()
        
dfs(1,0)