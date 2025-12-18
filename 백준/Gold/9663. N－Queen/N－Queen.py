n = int(input())

visit_col = [False] * n
visit_d1 = [False] * (2*n)
visit_d2 = [False] * (2*n)

arr = [[0] * n for _ in range(n)]

ans = 0

# 현재 배치한 q 수, 배열
def dfs(r):
    global n,ans
    if r == n:
        ans += 1
        return
    
    for c in range(n):
        if not visit_col[c] and not visit_d1[r+c] and not visit_d2[r-c+n]:
            visit_col[c] = True
            visit_d1[r+c] = True
            visit_d2[r-c+n] = True
            dfs(r+1)
            visit_col[c] = False
            visit_d1[r+c] = False
            visit_d2[r-c+n] = False
dfs(0)
print(ans)