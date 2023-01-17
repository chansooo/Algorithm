from math import ceil

kid_num, color_num = map(int, input().split())
gem_info = []
gem_max = 0
answer = float('inf')
for i in range(color_num):
    inp = int(input())
    gem_info.append(inp)
    gem_max = max(gem_max, inp)

start = 1
end = gem_max
while start <= end:
    mid = (start + end) // 2
    will_num = 0
    for gem in gem_info:
        will_num += ceil(gem / mid)
    if will_num > kid_num:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer, mid)
        
print(answer)

