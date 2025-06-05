def solution(n, l, r):
    ans = []
    for i in range(l,r+1):
        ans.append(max(i//n+1,i%n+1))
    return ans