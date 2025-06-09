def solution(n, s):
    ans = []
    if n > s: return [-1]
    q = s//n
    r = s%n
    for _ in range(r):
        ans.append(q+1)
    for _ in range(n-r):
        ans.append(q)
    ans.sort()
    return ans