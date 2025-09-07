from sys import stdin as input
from collections import deque,defaultdict
m,s = map(int,input.readline().split())
fish = defaultdict(list)
# 물고기 이동
directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
# 상어 이동
sd = [(-1,0),(0,-1),(1,0),(0,1)]
for _ in range(m):
    x,y,d = map(int,input.readline().split())
    x -= 1
    y -= 1
    d -= 1
    key = (x,y)
    fish[key].append(d)
smell = [[0] * 4 for _ in range(4)]
sx,sy = map(int,input.readline().split())
sx -= 1
sy -= 1
path = []
# 4*4*4
for i in range(4):
    for j in range(4):
        for k in range(4):
            path.append((i,j,k))

def check(x,y): return 0 <= x < 4 and 0 <= y < 4

def fish_move(key,idx,new_fish):
    global smell,sx,sy
    cx,cy = key
    for i in range(8):
        d = (idx-i) % 8
        nx,ny = cx + directions[d][0], cy + directions[d][1]
        if not check(nx,ny): continue
        if smell[nx][ny] > 0: continue
        if nx == sx and ny == sy: continue
        new_fish[(nx,ny)].append(d)
        return
    new_fish[(cx,cy)].append(idx)
    return

def shark_move(new_fish,turn):
    global path,smell,sx,sy
    # 가장 많이 먹는 물고기
    cnt = 0
    # 사전순 앞서는 거
    best = 10000
    moves = None
    bx,by = sx,sy

    for idx,p in enumerate(path):
        flag = True
        cx,cy = sx,sy
        # 잡아먹은 물고기
        eat = 0
        # 물고기가 있었던 칸(중복 방지를 위해 set)
        visit = set()
        for i in p:
            cx,cy = cx + sd[i][0], cy + sd[i][1]
            if not check(cx,cy):
                flag = False
                break
            # 물고기가 존재한다면 
            f = len(new_fish[(cx,cy)])
            if f > 0 and (cx,cy) not in visit:
                eat += f
                visit.add((cx,cy))
            
        # 유효하지 움직이 존재하면 pass
        if not flag: continue

        # 최대로 먹고 최소 사전 순인지 확인
        if eat > cnt or (eat == cnt and idx < best):
            cnt = eat
            best = idx
            moves = visit
            bx,by = cx,cy
    
    # 물고기 냄새 남기기 & 물고기 제거 & 상어 움직임 반영
    if moves != None:
        sx,sy = bx,by
        # print(f"최고의 움직임: {path[best]}")
        # print(f"잡아 먹은 물고기 수: {cnt}")
        # print(f"물고기 위치: {moves}")
        for x,y in moves:
            smell[x][y] = turn
            del new_fish[(x,y)]

turn = 1
for _ in range(s):
    # 모든 물고기 복제(깊은 복사)
    copy = defaultdict(list)
    for k in fish.keys():
        if fish[k]:
            for d in fish[k]:
                copy[k].append(d)
    # 모든 물고기 한 칸 이동
    # 상어가 있거나, 냄새나거나, 격자 벗어나면 x
    new_fish = defaultdict(list)
    for k in fish.keys():
        if fish[k]:
            for d in fish[k]:
                fish_move(k,d,new_fish)
    # 상어 이동, 물고기 제거 및 냄새 남기기
    shark_move(new_fish,turn)
    # 2턴 전 냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[i][j] == turn - 2:
                smell[i][j] = 0
    # 복제 반영
    for k,v in copy.items():
        new_fish[k].extend(v)
    fish = new_fish
    turn += 1

ans = 0
for v in fish.values():
    ans += len(v)
print(ans)