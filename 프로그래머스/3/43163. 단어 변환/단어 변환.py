from collections import deque
def solution(b, t, words):
    ans = 0
    q = deque()
    def check_d(str1, str2):
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))
    n = len(words)
    
    q.append((b, 0, [False] * n))
    while q:
        cur, cnt, visit = q.popleft()
        if cur == t:
            ans = cnt
            break
        for i in range(n):
            if not visit[i] and check_d(words[i], cur) == 1:
                visit[i] = True
                newV = visit[:]
                q.append((words[i], cnt + 1, newV))
    return ans