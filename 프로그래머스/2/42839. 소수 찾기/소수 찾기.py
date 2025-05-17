from itertools import permutations as perm
def minor(n):
    if n < 2:
        return False
    if n == 2: return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True
def solution(nums):
    ans = set()
    visit = set()
    # 1,2...len(nums)개
    for i in range(1,len(nums)+1):
        for c in perm(nums,i):
            n = int(''.join(c))
            if n in visit: continue
            visit.add(n)
            if minor(n): ans.add(n)
    return len(ans)