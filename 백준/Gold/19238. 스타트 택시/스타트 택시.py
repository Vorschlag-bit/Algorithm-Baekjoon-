from sys import stdin as input
from collections import deque
directions = [(0,1),(1,0),(0,-1),(-1,0)]
# 손님을 도착지에 데려다줄 때마다 연료 충전, 연료 없으면 끝
# m명의 승객 태우는 게 목표
# 특정 위치 이동 시 항상 최단 거리
# 승객은 한 명만 탑승 가능. 출발지에서만 탑승 가능. 목적지에서만 내리기 가능
# 승객을 고를 때 현재 위치에서 최단 거리에 있는 손님 태우기. 여러 명일 경우 최소 번호
# 연료는 한 칸 이동할 때마다 -1. 한 승객 이동 성공하면, 해당 승객 이동 소모 비용 * 2가 연료 충전됌.
# 승객을 목적지에 이동시킴과 동시에 연료가 바닥나면 성공으로 간주
# 모든 손님을 이동시키고 연료 충전까지 마친 후 남은 연료 출력. 연료 바닥 || 손님 이동 불가 || 목적지 이동 불가 시
# -1 출력
n,m,fuel = map(int,input.readline().split())
# 0은 빈칸, 1은 벽
arr = [list(map(int,input.readline().split())) for _ in range(n)]
# 0-based
sx,sy = map(int,input.readline().split())
sx -= 1
sy -= 1
# 목적지 도착한 손님
goal = [False] * m
# key = 손님 번호(0-base), value = (출발 좌표, 목적 좌표)
guest = dict()
for i in range(m):
    gsx,gsy,gtx,gty = map(int,input.readline().split())
    guest[i] = (gsx-1,gsy-1,gtx-1,gty-1)

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx,sy):
    global n,arr
    q = deque()
    visit = [[-1] * n for _ in range(n)]
    visit[sx][sy] = 0
    q.append((sx,sy))
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+directions[i][0], cy+directions[i][1]
            if not check(nx,ny): continue
            if arr[nx][ny] != 1 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[cx][cy] + 1
                q.append((nx,ny))
    
    return visit

remain = m
while remain > 0:
    # 데려갈 손님을 찾을 최소거리 map
    visit = bfs(sx,sy)
    candidate = []
    for i in range(m):
        if goal[i]: continue
        gsx,gsy,gtx,gty = guest[i]
        cur_d = visit[gsx][gsy]
        # 못 가면 패스
        if cur_d == -1: continue
        candidate.append((cur_d,gsx,gsy,i))
    
    if not candidate: break
    candidate.sort(key=lambda x: (x[0],x[1],x[2]))
    toGuest,gsx,gsy,idx = candidate[0]
    fuel -= toGuest
    if fuel < 0: break
    sx,sy = gsx,gsy
    # 손님을 목적지로 데려갈 map
    visit = bfs(sx,sy)
    gtx,gty = guest[idx][2:]
    # 손님을 도착지 못 데려가면 break
    if visit[gtx][gty] == -1: break
    fuel -= visit[gtx][gty]
    if fuel < 0: break
    fuel += visit[gtx][gty] * 2
    goal[idx] = True
    remain -= 1
    sx,sy = gtx,gty

if remain == 0:
    print(fuel)
else: print(-1)