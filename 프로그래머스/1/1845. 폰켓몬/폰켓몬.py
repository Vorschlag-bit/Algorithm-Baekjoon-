from collections import Counter
def solution(nums):
    n = len(nums) // 2
    cnt = Counter(nums)
    l = len(cnt.keys())
    return min(l,n)