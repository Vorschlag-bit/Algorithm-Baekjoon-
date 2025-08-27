from sys import stdin as input
n,k = map(int,input.readline().split())
# 말들 x,y 위치 저장할 dict(list), (말 번호, 방향)
h = dict()
direction = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
change = {1:2,2:1,3:4,4:3}
arr = [list(map(int,input.readline().split())) for _ in range(n)]
time = 1
# 말들 움직임을 기록할 3차원 맵
maps = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x,y,d = map(int,input.readline().split())
    h[i] = (x-1,y-1,d)
    maps[x-1][y-1].append(i)

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def white(cx,cy,nx,ny,i,d):
    idx = maps[cx][cy].index(i)
    temp = maps[cx][cy][idx:]
    maps[nx][ny].extend(temp)
    maps[cx][cy] = maps[cx][cy][:idx]
    # 이동한 말들 좌표 갱신
    for pid in temp:
        if pid == i: h[pid] = (nx,ny,d)
        else: h[pid] = (nx,ny,h[pid][2])

def red(cx,cy,nx,ny,i,d):
    # 뒤집기
    idx = maps[cx][cy].index(i)
    temp = maps[cx][cy][idx:][::-1]
    maps[nx][ny].extend(temp)
    maps[cx][cy] = maps[cx][cy][:idx]
    # 이동한 말들 좌표 갱신
    for pid in temp:
        if pid == i: h[pid] = (nx,ny,d)
        else: h[pid] = (nx,ny,h[pid][2])


while time < 1000:
    # 턴 와중에 말이 4개 이상 쌓이면 종료
    flag = True
    for i in range(k):
        # 움직일 때마다 해당 칸에 말이 있는지 파악하고, 있다면 쌓고 쌓인 모든 말에 대해서 nx,ny로 변경해줘야 함.
        cx,cy,d = h[i]
        nx,ny = cx+direction[d][0], cy+direction[d][1]
        # 파란색(범위 벗어나거나)
        if not check(nx,ny) or arr[nx][ny] == 2:
            d = change[d]
            nx,ny = cx+direction[d][0], cy+direction[d][1]
            if not check(nx,ny) or arr[nx][ny] == 2:
                h[i] = (cx,cy,d)
                continue
            # 그게 아니면 움직이기
            elif arr[nx][ny] == 0: white(cx,cy,nx,ny,i,d)
            else: red(cx,cy,nx,ny,i,d)
        #  하얀색
        elif arr[nx][ny] == 0:
            white(cx,cy,nx,ny,i,d)
        # 빨간색
        else:
            red(cx,cy,nx,ny,i,d)
        
        # 한 말이 움직임을 끝내고 4개 말이 자신의 위치에 쌓였는지 파악
        if len(maps[nx][ny]) >= 4:
            flag = False
            break

    if not flag:
        print(time)
        exit()
    time += 1

print(-1)