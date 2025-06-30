def solution(pn):
    l = len(pn) - 4
    ans = ''
    for i in range(l):
        ans += '*'
    for i in range(l,len(pn)):
        ans += pn[i]
    return ans