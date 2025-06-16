def dec2n(n):
    cnt = 0
    s = ''
    while n > 0:
        r = n % 2
        if r == 1: cnt += 1
        s = str(r) + s
        n //= 2
    return cnt

def solution(n):
    cnt = dec2n(n)
    for num in range(n+1,10000000):
        if dec2n(num) == cnt:
            return num