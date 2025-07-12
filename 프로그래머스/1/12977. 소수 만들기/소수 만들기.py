from itertools import combinations as comb
def minor(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True
def solution(nums):
    ans = 0
    
    for c in comb(nums,3):
        if minor(sum(c)): ans += 1

    return ans