n,m,x,y,k = map(int,input().split())

arr = []
# 남,북판별 리스트(상단,정면,바닥,뒤)
ns = [1,5,6,2]
# 동,서판별 리스트(정면 오른쪽, 정면 왼쪽)
ws = [4,3]
# 주사위 (1-6까지 초반엔 모두 0)
dice = [0,0,0,0,0,0,0]
# 주사위 이동방향(동=1,서=2,북=3,남=4)
direction = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

command = list(map(int,input().split()))

def check(x,y):
    return 0<= x < n and 0 <= y < m

for com in command:
    nx,ny = x + direction[com][0], y + direction[com][1]
    # 아웃이면 패스
    if not check(nx,ny): continue

    # 아닐 경우 주사위 회전
    # 동일 경우
    if com == 1:
        # 상단 <- 정오, 밑 <- 정왼, 정오 <- 밑, 정왼 <- 상단
        top = ns[0]
        bottom = ns[2]
        front_right = ws[0]
        front_left = ws[1]
        ns[0] = front_right
        ns[2] = front_left
        ws[0] = bottom
        ws[1] = top
    # 서일 경우
    elif com == 2:
        # 상단 <- 정왼, 밑 <- 정오, 정오 <- 상단, 정왼 <- 밑
        top = ns[0]
        bottom = ns[2]
        front_right = ws[0]
        front_left = ws[1]
        ns[0] = front_left
        ns[2] = front_right
        ws[0] = top
        ws[1] = bottom
    # 북일 경우
    elif com == 3:
        # 상단 <- 정면, 정면 <- 밑, 밑 <- 뒤, 뒤 <- 상단
        top = ns[0]
        front = ns[1]
        bottom = ns[2]
        back = ns[3]
        ns[0] = front
        ns[1] = bottom
        ns[2] = back
        ns[3] = top
    # 남일 경우
    elif com == 4:
        # 상단 <- 뒤, 정면 <- 상단, 밑 <- 정면, 뒤 <- 밑
        top = ns[0]
        front = ns[1]
        bottom = ns[2]
        back = ns[3]
        ns[0] = back
        ns[1] = top
        ns[2] = front
        ns[3] = bottom
    if arr[nx][ny] == 0:
        # 0이면 바닥면에 있는 수가 칸에 복사
        arr[nx][ny] = dice[ns[2]]
        # 상단 출력
        print(dice[ns[0]])
    else:
        # 0이 아니면 칸에 쓰인 수가 주사위 바닥에 복사, 칸에 적힌 수 = 0
        dice[ns[2]] = arr[nx][ny]
        arr[nx][ny] = 0
        print(dice[ns[0]])
    # 칸 이동
    x,y = nx,ny