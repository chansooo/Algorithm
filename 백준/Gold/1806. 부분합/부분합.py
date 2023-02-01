import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = float('inf')

while True:
    if sum >= s:
        min_length = min(min_length, right - left)
        sum -= numbers[left]
        left += 1
    elif right == n:
        break
    elif sum < s:
        sum += numbers[right]
        right += 1
    
if min_length == float('inf'):
    print(0)
else:
    print(min_length)