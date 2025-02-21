from collections import deque
def solution(n, coms):
    answer = 0
    visit = [False] * n
    
    def dfs(i):
        visit[i] = True
        for j in range(n):
            if not visit[j] and coms[i][j] == 1:
                dfs(j)
    
    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1
    
    return answer