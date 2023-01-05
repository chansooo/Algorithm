import sys

def solution(need_num, lans):
  start, end = 1, max(lans)
  n = len(lans)
  while start <= end:
    mid = (start + end) // 2
    output = 0
    for lan in lans:
      output += make_lan_num(lan, mid)
    if output < need_num:
      end = mid - 1
    else:
      start = mid + 1
  return end


def make_lan_num(lan_length, target_length):
  return lan_length // target_length

K, N = map(int, input().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]
print(solution(N, lans))

