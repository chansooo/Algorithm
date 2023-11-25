def convert(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

def is_prime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
def solution(n, k):
    s = convert(n, k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue
        if is_prime(int(num)): cnt += 1
    return cnt