from sys import stdin as input
from collections import defaultdict
# 맨 처음에 모든 상어가 자신 위치에 냄새 뿌리기
# 1초마다 동시에 상하좌우 인접한 칸으로 이동 후, 냄새 뿌리기. 냄새는 상어가 k번 이동하고 나면 사라진다.
# 상어의 이동 방향 결정 방식
# 1. 인접한 칸 중 냄새가 없는 칸의 방향
# 2. 그런 칸이 없으면 자신의 냄새가 있는 칸으로 방향
# 위 둘 방식으로 결정할 때, 우선순위가 있는데
# 우선순위는 상어마다 다를 수 있고, 현재 상어가 보고 있는 방향에 따라 다를 수 있다.
# 모든 상어가 이동 후, 한 칸에 여러 상어가 있다면, 가장 작은 번호의 상어만 남는다.
directions = [(-1,0),(1,0),(0,-1),(0,1)]
n,m,k = map(int,input.readline().split())
smell = [[0] * n for _ in range(n)]
l = [list(map(int,input.readline().split())) for _ in range(n)]
start_dir = [0]
sd = list(map(int,input.readline().split()))
# key = 상어 번호, value = x,y,dir
shark = dict()
# 0-base가 아니라 번호에 맞게 초기화
start_dir += sd
for i in range(n):
    for j in range(n):
        if l[i][j] != 0:
            num = l[i][j]
            # 번호, 냄새 기한
            smell[i][j] = (num,k)
            d = start_dir[num]
            shark[num] = (i,j,d-1)

# key = (상어 번호,방향), value = [우선순위 방향]
p = dict()
for i in range(m):
    # 상어 번호
    num = i + 1
    for j in range(4):
        # 위,아래,왼,오른 순
        key = (num,j)
        d = list(map(int,input.readline().split()))
        d = [number-1 for number in d]
        p[key] = d

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def counting(arr):
    # 격자에 상어 수 세기
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0: cnt += 1
    return cnt

def move_shark(shark):
    for num in shark.keys():
        cx,cy,cd = shark[num]
        move = False
        dirs = p[(num,cd)]
        # 냄새 없는 칸 찾아 이동
        for d in dirs:
            nx,ny = cx + directions[d][0], cy + directions[d][1]
            if not check(nx,ny): continue
            if smell[nx][ny] == 0:
                shark[num] = (nx,ny,d)
                move = True
                break

        # 자기 냄새 찾아 이동
        if move: continue

        for d in dirs:
            nx,ny = cx + directions[d][0], cy + directions[d][1]
            if not check(nx,ny): continue
            if smell[nx][ny][0] == num:
                shark[num] = (nx,ny,d)
                break

def min_shark(shark,new_pos):
    for num in shark.keys():
        x,y,d = shark[num]
        new_pos[(x,y)].append((num,d))
    
    new_shark = dict()
    for pos,shark_list in new_pos.items():
        # 번호 순으로 정렬
        shark_list.sort()
        min_s,sd = shark_list[0]
        x,y = pos
        new_shark[min_s] = (x,y,sd)
    # 덮어씌우기
    return new_shark  
        

def smell_remove(smell):
    for i in range(n):
        for j in range(n):
            if smell[i][j] != 0:
                if smell[i][j][1] == 1: smell[i][j] = 0
                else: smell[i][j] = (smell[i][j][0], smell[i][j][1]-1)

def get_shark(shark,smell):
    global k
    for num in shark.keys():
        x,y,d = shark[num]
        smell[x][y] = (num,k)

ans = 0
while ans <= 1000:
    if len(shark) == 1:
        print(ans)
        exit()
    # 상어 이동
    move_shark(shark)

    # 최소 번호 상어만 남기기
    # 이때 new_shark dict에 최신 상어 번호 및 위치 초기화
    new_pos = defaultdict(list)
    shark = min_shark(shark,new_pos)
    # 모든 상어 냄새 -1
    # !=0이고, != k인 거 -1
    # 0이 될 경우 해당 arr[i][j] = 0으로 초기화
    smell_remove(smell)

    # new_shark 돌면서 smell에 num,k 남기기
    get_shark(shark,smell)
    ans += 1

print(-1)