from sys import stdin as input
from collections import deque

n, k = map(int, input.readline().split())
# 최대 크기인 10만
Max = 100000
visit = [0] * (Max + 1)

def check(idx):
    global Max
    return 0 <= idx <= Max

def bfs(start):
    global k
    global Max
    q = deque()
    q.append((start, 0))
    while q:
        idx, sec = q.popleft()
        if idx == k:
            break
        # bfs를 이용한 완전 탐색
        else:
            # 이동할 지점 3가지
            n1, n2, n3 = idx + 1, idx * 2, idx - 1
            if check(n1) and visit[n1] == 0:
                visit[n1] = sec + 1
                q.append((n1, sec + 1))
            if check(n2) and visit[n2] == 0:
                visit[n2] = sec + 1
                q.append((n2, sec + 1))
            if check(n3) and visit[n3] == 0:
                visit[n3] = sec + 1
                q.append((n3, sec + 1))
bfs(n)
print(visit[k])