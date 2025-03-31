n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
direction = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 1000
def check(nx,ny):
    return 0 <= nx < n and 0 <= ny < m

def No5(x,y,arr):
    cx, cy = x,y
    for d in range(4):
        nx,ny = cx, cy 
        while check(nx,ny):
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = '#'
            else: pass
            nx,ny = nx + direction[d][0], ny + direction[d][1]

no5list = []
for i in range(n):
    for j in range(m):
        if  0 < arr[i][j] < 5:
            cctv.append((i,j))
        elif arr[i][j] == 5:
            no5list.append((i,j))
# 5번부터 먼저 초기화
for numbers in no5list:
    a,b = numbers[0],numbers[1]
    No5(a,b,arr)


def No4(x,y,d,copy):
    obs = 0
    # 3가지 방향으로 관측해야 함
    # 1번(기존 방향 d), 2번((d+3)%4), 3번((d+1)%4)을 유지하면서 배열끝까지 탐색
    x1,y1 = x+direction[d][0],y+direction[d][1]
    x2,y2 = x+direction[(d+3)%4][0],y+direction[(d+3)%4][1]
    x3,y3 = x+direction[(d+1)%4][0],y+direction[(d+1)%4][1]
    while check(x1,y1):
        if copy[x1][y1] == 6: break
        elif copy[x1][y1] == 0:
            copy[x1][y1] = '#'
            obs += 1
        else: pass
        x1,y1 = x1 + direction[d][0], y1+direction[d][1]
    while check(x2,y2):
        if copy[x2][y2] == 6: break
        elif copy[x2][y2] == 0:
            copy[x2][y2] = '#'
            obs += 1
        else: pass
        x2,y2 = x2+direction[(d+3)%4][0],y2+direction[(d+3)%4][1]
    while check(x3,y3):
        if copy[x3][y3] == 6: break
        elif copy[x3][y3] == 0:
            copy[x3][y3] = '#'
            obs += 1
        else: pass
        x3,y3 = x3+direction[(d+1)%4][0],y3+direction[(d+1)%4][1]
    return obs

def No3(x,y,d,copy):
    obs = 0
    # 1번(기존 방향 d), 2번((d+3)%4), 3번((d+1)%4)을 유지하면서 배열끝까지 탐색
    x1,y1 = x+direction[d][0],y+direction[d][1]
    x2,y2 = x+direction[(d+3)%4][0],y+direction[(d+3)%4][1]
    while check(x1,y1):
        if copy[x1][y1] == 6: break
        elif copy[x1][y1] == 0:
            copy[x1][y1] = '#'
            obs += 1
        else: pass
        x1,y1 = x1 + direction[d][0], y1+direction[d][1]
    while check(x2,y2):
        if copy[x2][y2] == 6: break
        elif copy[x2][y2] == 0:
            copy[x2][y2] = '#'
            obs += 1
        else: pass
        x2,y2 = x2+direction[(d+3)%4][0],y2+direction[(d+3)%4][1]
    return obs

def No2(x,y,d,copy):
    obs = 0
    x1,y1 = x+direction[d][0],y+direction[d][1]
    x2,y2 = x+direction[(d+2)%4][0],y+direction[(d+2)%4][1]
    while check(x1,y1):
        if copy[x1][y1] == 6: break
        elif copy[x1][y1] == 0:
            copy[x1][y1] = '#'
            obs += 1
        else: pass
        x1,y1 = x1 + direction[d][0], y1+direction[d][1]
    while check(x2,y2):
        if copy[x2][y2] == 6: break
        elif copy[x2][y2] == 0:
            copy[x2][y2] = '#'
            obs += 1
        else: pass
        x2,y2 = x2+direction[(d+2)%4][0],y2+direction[(d+2)%4][1]
    return obs

def No1(x,y,d,copy):
    obs = 0
    x1,y1 = x+direction[d][0],y+direction[d][1]
    while check(x1,y1):
        if copy[x1][y1] == 6: break
        elif copy[x1][y1] == 0:
            copy[x1][y1] = '#'
            obs += 1
        else: pass
        x1,y1 = x1 + direction[d][0], y1+direction[d][1]
    return obs

perms = []

def perm(n,new_arr):
    if len(new_arr) == n:
        perms.append(new_arr[:])
        return
    for i in range(4):
        perm(n,new_arr + [i])
perm(len(cctv),[])

for product in perms:
    copy = [row[:] for row in arr]
    for idx,c in enumerate(cctv):
        # 각 cctv마다 product의 값으로 회전
        No = copy[c[0]][c[1]]
        if No == 1:
            No1(c[0],c[1],product[idx],copy)
        elif No == 2:
            No2(c[0],c[1],product[idx],copy)
        elif No == 3:
            No3(c[0],c[1],product[idx],copy)
        else:
            No4(c[0],c[1],product[idx],copy)
    eachMin = 0
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                eachMin += 1
    ans = min(ans,eachMin)

print(ans)