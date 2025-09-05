from sys import stdin as input
from collections import deque
# 주사위 윗면 1, 동쪽 3인 상태로 0,0에서 시작
# 1. 주사위는 한 칸 굴러감. 만약 이동 방향에 칸이 없다면 반대 방향으로 한 칸 굴러감.
# 2. 주사위 아랫면에 있는 정수 a와 주사위가 있는 칸(x,y)에 있는 정수 b를 비교해 이동.
# a > b인 경우, 이동 방향을 시계 방향 90도 회전
# a < bd인 경우, 반시계 90도 회전
# 같다면 이동 방향 유지
# 점수 계산 => x,y의 b * 4방향 갈 수 있는 칸의 수의 합인 c
directions = [(0,1),(0,-1),(1,0),(-1,0)]
n,m,k = map(int,input.readline().split())
arr =[list(map(int,input.readline().split())) for _ in range(n)]
# 0,1,2,3 동서남북 순
d = 0
# 반대 방향
cc = {0:1,1:0,2:3,3:2}
# 시계방향
clock = {0:2,2:1,1:3,3:0}
counter = {0:3,3:1,1:2,2:0}
dx,dy = 0,0
# 위,앞,밑,뒤,왼,오
dice = [1,5,6,2,4,3]
ans = 0
def check(x,y):
    return 0 <= x < n and 0 <= y < m

def roll_east():
    global dice
    # 뒤,앞빼고 바뀜(1,3)
    dice[0],dice[2],dice[4],dice[5] = dice[4],dice[5],dice[2],dice[0]
def roll_west():
    global dice
    # 뒤,앞빼고 바뀜(1,3)
    dice[0],dice[2],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[2]
def roll_south():
    global dice
    # 왼,오빼고 바뀜(4,5)
    dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]
def roll_north():
    global dice
    dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
def get_score(x,y):
    global arr
    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True
    num = arr[x][y]
    q = deque()
    cnt = 1
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        for nd in directions:
            nx,ny = cx + nd[0], cy + nd[1]
            if check(nx,ny) and not visit[nx][ny] and num == arr[nx][ny]:
                visit[nx][ny] = True
                cnt += 1
                q.append((nx,ny))
    return cnt

for _ in range(k):
    nx,ny = dx + directions[d][0], dy + directions[d][1]
    if not check(nx,ny):
        # 방향 반대
        d = cc[d]
        nx,ny = dx + directions[d][0], dy + directions[d][1]
    if d == 0: roll_east()
    elif d == 1: roll_west()
    elif d == 2: roll_south()
    else: roll_north()
    # 점수 계산
    dx,dy = nx,ny
    b = arr[dx][dy]
    c = get_score(dx,dy)
    ans += b * c
    # 다음 이동 방향 결정
    # 아랫면 숫자
    a = dice[2]
    # 정수 b
    if a > b:
        d = clock[d]
    elif a < b:
        d = counter[d]
print(ans)