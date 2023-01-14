n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] == 2:
        arr[i] = -1

prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

answer = max(prefix_sum) - min(prefix_sum)
answer = max(answer, 0)
print(answer)
