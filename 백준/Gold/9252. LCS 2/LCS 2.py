str1 = input()
str2 = input()

len1, len2 = len(str1), len(str2)
# i, j만큼 갔을 때 최대값과 string을 저장.
dp = [[''] * (len2 + 1) for _ in range(len1 + 1)]



for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))

print(dp[-1][-1])