from sys import stdin as input
# 행,열은 원형으로 연결되어 있음
# 비바라기 시전 시, (n-1,0), (n-1,1), (n-2,0), (n-2,1)에 비구름 생성
# 0-based 8개 방향
directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
# 대각선
cross = [(-1,-1),(1,-1),(1,1),(-1,1)]
# m번의 명령
# 1. 모든 구름들이 d방향으로 s칸 이동
# 2. 각 구름에서 비가 내려, 구름 칸 바구니에 물 양 + 1
# 3. 구름 모두 사라짐
# 4. 2에서 물이 증가한 칸(i,j)에 물복사, 물복사는 '대각선 방향' 거리가 1인 칸에 있는 물의 수만큼
# (i,j)에 증가. 이때 이동과는 다르게 경계 넘어서면 인정 x
# 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 해당 칸 물 -2.
# 이때 구름이 생성되는 칸은 3에서 사라진 칸이 아님.
# m번의 명령 후 바구니의 물의 양 합
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
clouds = set([(n-1,0), (n-1,1), (n-2,0), (n-2,1)])
cmd = []
for _ in range(m):
    d,s = map(int,input.readline().split())
    # 0-based
    cmd.append((d-1,s))

def check(x,y):
    return 0 <= x < n and 0 <= y < n

for d,s in cmd:
    # 모든 구름 d방향 s칸 이동
    new_cloud = set()
    for x,y in clouds:
        nd = directions[d]
        nx,ny = (x+nd[0]*s) % n, (y+nd[1]*s) % n
        new_cloud.add((nx,ny))
    # 각 구름에서 비내리기
    for x,y in new_cloud:
        arr[x][y] += 1
    # 구름 칸에서 물복사
    for x,y, in new_cloud:
        for nd in cross:
            nx,ny = x + nd[0], y + nd[1]
            if check(nx,ny) and arr[nx][ny] > 0:
                arr[x][y] += 1
    # 2이상인 곳에서 구름 생성
    n_cloud = set()
    for i in range(n):
        for j in range(n):
            # 이동 전과 이동한 구름 칸이 아니어야 함
            key = (i,j)
            if arr[i][j] >= 2 and key not in new_cloud:
                n_cloud.add((i,j))
                arr[i][j] -= 2
    # 덮어씌우기
    clouds = n_cloud
ans = 0
for i in range(n):
    for j in range(n):
        ans += arr[i][j]
print(ans)