from collections import deque
def solution(b, m):
    # 인덱스화
    m = [x-1 for x in m]
    q = deque()
    n = len(b)
    answer = 0
    for i in m:
        for j in range(n):
            if b[j][i] != 0:
                q.append(b[j][i])
                b[j][i] = 0
                break
        while len(q) >= 2:
            if q[-1] == q[-2]:
                answer += 2
                q.pop()
                q.pop()
            else:
                break
    return answer