str1 = input()
str2 = input()

len1, len2 = len(str1), len(str2)
dp = [[0]* (len2+1) for _ in range(len1+1)]

for i in range(len1+1):
    for j in range(len2+1):
        if i == 0 or j == 0:
            dp[i][j] == 0
        elif str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[-1][-1])