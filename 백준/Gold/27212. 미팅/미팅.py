N, M, C = map(int, input().split())
W = []
for i in range(C):
    W.append(list(map(int, input().split())))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        ans1 = W[A[i]-1][B[j]-1] + dp[i][j]

        ans2 = dp[i][j+1]

        ans3 = dp[i+1][j]
        
        dp[i+1][j+1] = max(ans1, ans2, ans3)

print(dp[N][M])