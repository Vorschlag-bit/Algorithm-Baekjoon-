import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline

def check(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def bfs(x, y, start):
    q = deque()
    q.append((x, y, start))  # 튜플로 묶어서 전달

    while q:
        cur_x, cur_y, num = q.popleft()
        if len(num) == 6:
            result_set.add(num)
            continue  # 6자리가 되면 더 이상 진행하지 않음
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if check(nx, ny):
                q.append((nx, ny, num + str(arr[nx][ny])))

arr = [list(map(int, input().split())) for _ in range(5)]
result_set = set()

for i in range(5):
    for j in range(5):
        start = str(arr[i][j])
        bfs(i, j, start)

print(len(result_set))