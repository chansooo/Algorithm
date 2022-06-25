T = int(input())
for _ in range(T):
  N = int(input())
  coin = list(map(int, input().split()))
  val = int(input())

  dest = [0 for _ in range(val+1)]
  dest[0] = 1
  for i in coin:
    for j in range(1,val+1):
      if j-i >= 0:
        dest[j] += dest[j-i]
  print(dest[val])