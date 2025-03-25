n = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
# 사과 위치를 저장할 map
for i in range(k):
    x,y = map(int, input().split())
    arr[x][y] = 1
l = int(input())
# 이동방향을 저장할 map
dir = dict()
for i in range(l):
    # sec 초 뒤 d방향으로 뱀 '머리'가 이동(L = 왼쪽, D = 오른쪽로 90도 회전)
    sec, d = input().split()
    dir[int(sec)] = d
# 1초부터 시작
s = 0
snake = [(1,1)]
# 우, 하, 좌, 상
direction = [(0,1),(1,0),(0,-1),(-1,0)]
def check(x,y):
    return 1 <= x <= n and 1 <= y <= n
cur_dir = 0
while True:
    # 기본적으로 뱀은 오른쪽으로 향함
    cx,cy = snake[-1]
    nx,ny = cx + direction[cur_dir][0], cy + direction[cur_dir][1]
    # 밖으로 나가면 끝
    if not check(nx,ny):
        print(s+1)
        exit()
    # 몸이랑 맞으면 끝
    if (nx,ny) in snake:
        print(s+1)
        exit()
    # 사과있는지 판단하기(꼬리 움직임 결정)
    flag = False
    if arr[nx][ny] == 1:
        flag = True
        arr[nx][ny] = 0
    # 몸통부터 꼬리까지 이동
    if flag:
        # 사과를 먹었으면 머리만 새로 추가
        snake.append((nx,ny))
    else:
        # 사과를 안 먹었으면 머리부터 꼬리까지 1칸씩 이동
        # 현재 머리 = nx,ny, 과거 머리 = cx,cy
        for idx in range(len(snake)-1,-1,-1):
            bx,by = snake[idx]
            snake[idx] = nx,ny
            nx,ny = bx,by
    # 머리 방향 바꾸기
    s += 1
    if s in dir.keys():
        if dir[s] == 'L':
            cur_dir = (cur_dir - 1) % 4
        else:
            cur_dir = (cur_dir + 1) % 4