import sys
sys.setrecursionlimit(10**7)

dp_list = [0]* 10001
test = []
modul = 1000000007
def dp(x):
  if x == 0: return 1
  if x == 1: return 0
  if x == 2: return 0
  if x == 3: return 3
    
  if dp_list[x] != 0: 
    return dp_list[x]
  
  result = (3 * dp(x-3))%modul
  for i in range(4, x+1):
    if i%3 == 0:
      result = (result + (4 * dp(x - i)))%modul

  return result


# T = int(input())

# for _ in range(T):
#   test.append(int(input()))

#for i in range(T):
#  print(dp(i))

i = int(input())
print(dp(i))





