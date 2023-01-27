from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
# print(nums)
ret = list(permutations(nums, m))

for r in ret:
    print(' '.join(map(str, r)))
