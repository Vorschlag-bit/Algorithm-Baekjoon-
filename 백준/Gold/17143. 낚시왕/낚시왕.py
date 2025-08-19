from sys import stdin as input
from collections import defaultdict

r, c, m = map(int, input.readline().split())

directions = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]
change = {1:2, 2:1, 3:4, 4:3}
sharks = defaultdict(list)

def move_shark(x,y,s,d):
    # 상하
    if d <= 2:
        cycle = 2 * (r-1)
        s = s % cycle
        for _ in range(s):
            # 위로
            if d == 1:
                if x == 0:
                    d = 2
                    x += 1
                else: x -= 1
            # 아래로
            else:
                if x == r - 1:
                    d = 1
                    x -= 1
                else: x += 1
    # 좌우
    else:
        cycle = 2 * (c-1)
        s = s % cycle
        for _ in range(s):
            # 우로
            if d == 3:
                if y == c - 1:
                    d = 4
                    y -= 1
                else: y += 1
            # 좌로
            else:
                if y == 0:
                    d = 3
                    y += 1
                else: y -= 1
    return x,y,d

for _ in range(m):
    x, y, s, d, z = map(int, input.readline().split())
    sharks[(x-1, y-1)].append((s, d, z))

pos = 0
ans = 0

for pos in range(c):  # 0부터 c-1까지
    # 낚시 시작
    for i in range(r):
        key = (i, pos)
        if sharks[key]:
            s, d, z = sharks[key][0]
            ans += z
            sharks[key] = []
            break
    
    # 상어 이동
    new_pos = defaultdict(list)
    for (x, y), shark_list in sharks.items():
        if shark_list:
            s, d, z = shark_list[0]
            nx, ny, nd = move_shark(x, y, s, d)
            new_pos[(nx, ny)].append((s, nd, z))
    
    # 상어 잡아먹기 (같은 위치에 여러 상어가 있을 때)
    for (x, y), shark_list in new_pos.items():
        if len(shark_list) > 1:
            # 크기가 가장 큰 상어만 남김
            max_shark = max(shark_list, key=lambda shark: shark[2])
            new_pos[(x, y)] = [max_shark]
    
    sharks = new_pos

print(ans)