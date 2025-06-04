import math
def dec2k(n,base):
    s = ''
    while n > 0:
        num = n % base
        s = str(num) + s
        n //= base
    return s

def check(n):
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
def solution(n, k):
    p = []
    base = dec2k(n,k)
    for s in base.split('0'):
        if not s: continue
        if check(int(s)): p.append(s)
    return len(p)