
from collections import defaultdict

n = int(input())
num_list = map(int, input().split())

num_dict = defaultdict(int)
for num in num_list:
    num_dict[num] += 1

m = int(input())
want_list = map(int, input().split())
answer = [num_dict[num] for num in want_list]
print(' '.join(map(str, answer)))