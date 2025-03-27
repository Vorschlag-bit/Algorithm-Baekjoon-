from collections import deque

n,m = map(int, input().split())
# 현재 방향에서 반시계로 돌면서 다 확인하는 방법은?
# 예: 1(동), 0 -> 3 -> 2 -> 1
# 예: 2(남), 2 -> 1 -> 0 -> 3
# 0 = 북, 1 = 동, 2 = 남, 3 = 서
# 회전은 반시계 90도 ex) 북 -> 서 -> 남 -> 동 -> 북 = (d + 3) % 3
direction = [(-1,0),(0,1),(1,0),(0,-1)]
r,c,d = map(int, input().split())
q = deque()
q.append((r,c,d))
arr = [list(map(int ,input().split())) for _ in range(n)]
ans = 0
def check(x,y):
    return 0<= x < n and 0<= y < m
# 1이면 벽, 0이면 청소 안 됨
while q:
    x,y,d = q.popleft()
    # 청소가 안 되어 있다면 청소
    if arr[x][y] == 0:
        arr[x][y] = -1
        ans += 1
    # 4군데 중 청소할 곳이 있는 판단하는 flag
    flag = False
    # 0 북 -> 반시계로 돌면서 방향을 확인해야 함...
    for i in range(d-1,d-5,-1):
        i = (i+4) % 4
        nx,ny = x + direction[i][0], y + direction[i][1]
        if not check(nx,ny) or arr[nx][ny] == 1:
            continue
        # 청소할 곳이 있으면 flag = True
        if arr[nx][ny] == 0:
            q.append((nx,ny,i))
            flag = True
            break
    # 청소할 곳이 없다면 바라보는 방향 유지한 채로 -1(반대로 움직이기)
    if not flag:
        di = (d+2) % 4
        nx,ny = x + direction[di][0], y + direction[di][1]
        if not check(nx,ny) or arr[nx][ny] == 1:
            print(ans)
            exit()
        q.append((nx,ny,d))