from sys import stdin as input
from collections import deque
# 처음 모든 칸 온도 = 0
# 1. 집에 있는 모든 온풍기에서 바람이 나옴.
# 2. 온도 조절
# 3. 온도가 1이상인 가장 바깥 온도가 1씩 감소
# 4. 초쿨릿 먹기
# 5. 조사하는 모든 칸의 온도가 k 이상이 되었는지 검사. 모든 칸 온도가 k 이상이면 중단. 
# 아니면 1부터 반복
# 온풍기는 4방향으로 작동
r,c,k = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(r)]
# 1 = 오른 방향 온풍기, 2 - 왼 방향 온풍기, 3 - 위 방향 온풍기, 4 - 아래 방향 온풍기, 5 - 온도 조사
directions = [(0,1),(0,-1),(-1,0),(1,0)]
# 오른/왼 = 0, 위/아래 = 1
turn = [[(-1,0),(0,0),(1,0)],[(0,1),(0,0),(0,-1)]]
ans = 0
temp = [[0] * c for _ in range(r)]
w = int(input.readline())
wall = set()

for _ in range(w):
    x,y,t = map(int,input.readline().split())
    x -= 1
    y -= 1
    # t = 0 -> (x,y)와 (x-1,y) 사이에 벽
    if t == 0:
        wall.add((x,y,x-1,y))
        wall.add((x-1,y,x,y))
    # t = 1 -> (x,y)와 (x,y+1) 사이에 벽
    else:
        wall.add((x,y,x,y+1))
        wall.add((x,y+1,x,y))
# 조사해야 하는 칸
route = []
# k = 좌표, v = 방향
warmer = dict()
for i in range(r):
    for j in range(c):
        key = (i,j)
        if arr[i][j] == 1:
            warmer[key] = 0
        elif arr[i][j] == 2:
            warmer[key] = 1
        elif arr[i][j] == 3:
            warmer[key] = 2
        elif arr[i][j] == 4:
            warmer[key] = 3
        elif arr[i][j] == 5: route.append((i,j))
# 가장 바깥쪽 루트
path = set()
for i in range(r):
    path.add((i,0))
    path.add((i,c-1))
for j in range(c):
    path.add((0,j))
    path.add((r-1,j))

def check(x,y):
    return 0 <= x < r and 0 <= y < c

def block(a,b,c,d):
    global wall
    return (a,b,c,d) in wall

def reach(cx,cy,nx,ny,nd,direction):
    # 현재 위치에서 nx,ny로 바람이 불 수 있는지 확인
    dx,dy = nd
    # 직진
    if dx == 0 and dy == 0:
        return not block(cx,cy,nx,ny)
    # 대각선
    # 1. x,y와 중간지점
    mx,my = cx + nd[0], cy + nd[1]
    # 중간 지점과 막혀있다면 false
    if block(cx,cy,mx,my): return False
    # 2. 중간지점과 nx,ny
    return not block(mx,my,nx,ny)

def wind(sx,sy,d):
    global wall,temp
    # 5가 나오는 곳
    nx,ny = sx + directions[d][0], sy + directions[d][1]
    # 막혀있다면 패스
    if not check(nx,ny) or block(sx,sy,nx,ny): return
    # 온도 중복 계산을 방지하기 위한 배열
    visit = [[False] * c for _ in range(r)]
    q = deque()
    # 첫 칸은 5
    q.append((nx,ny,5))
    temp[nx][ny] += 5
    visit[nx][ny] = True
    while q:
        cx,cy,h = q.popleft()
        # 다음 열이 1이면 pass
        if h < 2: continue
        
        # 0,1이면 오른/왼, 2,3이면 위/아래
        type = turn[0] if d < 2 else turn[1]
        # 3개의 방향 탐색
        x,y = cx + directions[d][0], cy + directions[d][1]
        for nd in type:
            nx,ny = x + nd[0], y + nd[1]
            if not check(nx,ny): continue
            # 중복 방지
            if visit[nx][ny]: continue
            if reach(cx,cy,nx,ny,nd,d):
                temp[nx][ny] += h - 1
                visit[nx][ny] = True
                q.append((nx,ny,h-1))

def cal_temp(temp):
    change = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for nd in directions:
                nx,ny = i + nd[0], j + nd[1]
                if not check(nx,ny) or block(i,j,nx,ny): continue
                h = temp[i][j]
                nh = temp[nx][ny]
                if h > nh:
                    diff = (h - nh) // 4
                    change[i][j] -= diff
                    change[nx][ny] += diff
    # 한 번에 반영
    for i in range(r):
        for j in range(c):
            temp[i][j] += change[i][j]


while ans < 101:
    # 모든 온풍기에서 각 방향에 맞춰 바람
    for (x,y) in warmer.keys():
        d = warmer[(x,y)]
        wind(x,y,d)
    # 온도 조절
    cal_temp(temp)

    # 가장 바깥쪽 1 감소
    for x,y in path:
        if temp[x][y] > 0: temp[x][y] -= 1
    # 쵸콜릿 먹기
    ans += 1
    # 모든 칸 온도가 k이상인지 체크
    flag = True
    for x,y in route:
        if temp[x][y] < k:
            flag = False
            break
    if flag: break
print(ans)