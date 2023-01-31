
n = int(input())
liquids = list(map(int, input().split()))


start = 0
end = n - 1

cur_ans = float('inf')
ans = []


while start < end:
    left = liquids[start]
    right = liquids[end]
    if abs(left + right) < cur_ans:
        cur_ans = abs(left + right)
        ans = [left, right]
    
    if left + right > 0:
        end -= 1
    elif left + right < 0:
        start += 1
    elif left + right == 0:
        break

print(*ans)