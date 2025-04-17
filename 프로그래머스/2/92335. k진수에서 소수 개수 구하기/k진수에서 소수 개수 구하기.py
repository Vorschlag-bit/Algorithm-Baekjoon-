import math
def dec2n(num,base):
    s = ''
    while num > 0:
        d = num % base
        s = str(d) + s
        num //= base
    return int(s)

def judge(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    g = dec2n(n,k)
    primary = []
    p = ''
    
    for num in str(g).split('0'):
        if not num: continue
        if judge(int(num)):
            primary.append(num)
        
    return len(primary)