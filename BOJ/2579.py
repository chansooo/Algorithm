stair_count = int(input())
stair_value_list = [int(input()) for _ in range(stair_count)]


dp = [0] * (stair_count+1)

dp[0] = stair_value_list[0]
dp[1] = stair_value_list[0] + stair_value_list[1]
dp[2] = max(stair_value_list[1] + stair_value_list[2], stair_value_list[0] + stair_value_list[2])
    

for i in range(3, stair_count):
    dp[i] = max(dp[i - 3] + stair_value_list[i - 1] + stair_value_list[i], dp[i - 2] + stair_value_list[i])
print(dp[stair_count - 1])

