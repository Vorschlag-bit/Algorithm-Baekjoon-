def cnt(n):
    if n == 1: return False
    if n == 2: return True
    sq = int(n**0.5)
    for num in range(2,sq + 1):
        if n % num == 0: 
            return False
    return True
def solution(n):
    ans = 0
    for num in range(1,n+1):
        if cnt(num):
            ans += 1
    return ans