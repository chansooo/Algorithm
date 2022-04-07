MOD = 1000000007
MAX = 10000
dp_list = [0] * 10000

def dp():
  i = 9

  while i < MAX:
    dp_list[i] = (((5 * dp_list[i - 3]) % MOD) + MOD - ((3 * dp_list[i - 6]) % MOD) + dp_list[i - 9]) % MOD

    i += 3




dp_list[0] = 1
dp_list[3] = 3
dp_list[6] = 13

dp()

T = int(input())



for i in range(T):
  a = int(input())
  if a%3 != 0:
    print(0)
  else:
    print(dp_list[a])



