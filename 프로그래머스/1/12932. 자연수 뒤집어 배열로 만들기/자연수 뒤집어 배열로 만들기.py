def solution(n):
    ans = []
    n = str(n)
    for i in range(len(n)-1,-1,-1):
        ans.append(int(n[i]))
    return ans
