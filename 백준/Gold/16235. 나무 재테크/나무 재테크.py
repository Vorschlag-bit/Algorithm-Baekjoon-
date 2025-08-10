from sys import stdin as input
from collections import defaultdict

n,m,k = map(int,input.readline().split())
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

# 시간에 따라 변할 양분
arr = [[5] * n for _ in range(n)]
# 양분 저장
source = [list(map(int,input.readline().split())) for _ in range(n)]
# (r,c)를 key로 사용하는 list dict
tree = defaultdict(list)
for _ in range(m):
    # z는 나이
    x,y,z = map(int,input.readline().split())
    tree[(x-1,y-1)].append(z)
# 처음 한 번만 정렬
for lst in tree.values():
    lst.sort()

ans = 0

def spring_summer(tree):
    # 영양소 dict(k - pos, value - v)
    dead = defaultdict(int)
    # 봄
    for pos,trees in tree.items():
        x,y = pos
        alive = []
        for idx,t in enumerate(trees):
            if arr[x][y] >= t:
                arr[x][y] -= t
                t += 1
                alive.append(t)
            else:
                dead[pos] += sum(dt // 2 for dt in trees[idx:])
                break
        tree[pos] = alive
    # 여름
    for (x,y), v in dead.items():
        arr[x][y] += v

def fall(tree):
    # 나이가 5배수인 나무만 directions 위치에 번식
    # 새로 생긴 나무 (k - pos, v - cnt)
    births = defaultdict(int)
    for pos,trees in tree.items():
        cx,cy = pos
        for t in trees:
            if t % 5 == 0:
                for d in directions:
                    nx,ny = cx+d[0],cy+d[1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 1살짜리 나무 번식
                        births[(nx,ny)] += 1
    # 한번에 추가
    for pos, v in births.items():
        tree[pos] = [1 for _ in range(v)] + tree[pos]

def winter():
    for i in range(n):
        for j in range(n):
            arr[i][j] += source[i][j]

for _ in range(k):
    # spring(어린 나무부터 양분 먹고, 양분 == 0이면 나머지 다 죽음)
    spring_summer(tree)

    # fall
    fall(tree)

    # winter
    winter()

print(sum(len(v) for v in tree.values()))