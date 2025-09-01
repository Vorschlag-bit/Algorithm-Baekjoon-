from sys import stdin as input
# 상어는 (0,0)의 물고기를 잡어먹고 시작(해당 물고기 방향 유지)
# 물고기 이동은 번호 오름차순
# 다음 칸에 상어 or 범위 넘으면 이동 불가
# 이동 불가 시 이동 방향 45도 반시계 회전, 모든 이동 방향 다 탐색해도 안 되면 이동 x
# 물고기가 다른 물고기 칸으로 이동 시 서로간의 위치 교환
# 물고기 이동이 끝나면 상어 이동 시작, 여러 칸 이동 가능, 물고기 칸으로만 이동 가능
# 물고기칸으로 이동 시, 해당 물고기 먹고 방향 갖기, 이동 시 지나가는 칸 물고기는 안 잡아먹지~
# 상어가 이동할 수 없으면 끝
directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
arr = [[0] * 4 for _ in range(4)]
ans = 0
f = dict()
for r in range(4):
    l = list(map(int,input.readline().split()))
    # 0,2,4,6
    for i in range(4):
        idx = i*2
        a = l[idx]
        b = l[idx+1] - 1
        arr[r][i] = (a,b)
        # a번 물고기 -> x,y,dir
        f[a] = (r,i,b)

# 0,0에 처음 먹힌 물고기 번호
start = arr[0][0][0]
start_dir = arr[0][0][1]
arr[0][0] = 0

def check(x,y):
    return 0 <= x < 4 and 0 <= y < 4

# 백트래킹
def dfs(sx,sy,sd,total,arr):
    global ans
    # 물고기 번호 순으로 움직이기
    fish = dict()
    for i in range(4):
        for j in range(4):
            # 상어는 패스
            if i == sx and j == sy: continue
            if arr[i][j] != 0:
                a,b = arr[i][j]
                fish[a] = (i,j,b)
    if len(fish.keys()) == 0:
        ans = max(ans, total)
        return
    # 물고기 이동 상태 복구를 하기 힘드므로 각 분기 별 새로운 배열 사용
    new_arr = [a[:] for a in arr]
    # 물고기 번호 순으로 이동
    number = sorted(fish.keys())
    for n in number:
        cx,cy,d = fish[n]
        # d방향으로 움직이기
        for i in range(8):
            nd = d + i
            nd %= 8
            nx,ny = cx + directions[nd][0], cy + directions[nd][1]
            # 다음 이동 방향이 벗어나거나, 상어가 있으면 안 됌
            if not check(nx,ny): continue
            if nx == sx and ny == sy: continue
            # 비어있거나 다른 물고기가 있을 경우 그대로 교환
            temp = new_arr[nx][ny]
            new_arr[nx][ny] = (n,nd)
            new_arr[cx][cy] = temp
            # 기준 물고기의 위치 옮기기
            if temp != 0:
                en,ed = temp[0],temp[1]
                fish[en] = (cx,cy,ed)
            fish[n] = (nx,ny,nd)
            break
    # 상어 이동
    tx,ty = sx + directions[sd][0], sy + directions[sd][1]
    move = False
    while True:
        if not check(tx,ty): break
        if new_arr[tx][ty] != 0:
            num,fish_dir = new_arr[tx][ty]
            new_arr[tx][ty] = 0
            move = True
            dfs(tx,ty,fish_dir,total + num,new_arr)
            new_arr[tx][ty] = (num,fish_dir)
        tx += directions[sd][0]
        ty += directions[sd][1]

    if not move:
        ans = max(total,ans)
        return

dfs(0,0,start_dir,start,arr)
print(ans)