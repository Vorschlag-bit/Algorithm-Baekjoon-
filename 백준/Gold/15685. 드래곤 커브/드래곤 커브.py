n = int(input())
arr = [[0] * 101 for _ in range(101)]
# east, north, west, south
direction = [(0,1),(-1,0),(0,-1),(1,0)]
ans = 0
command = [list(map(int, input().split())) for _ in range(n)]
for c in command:
    y,x,d,g = c[0],c[1],c[2],c[3]
    arr[x][y] += 1
    dragon = []
    dragon.append(d)
    # 드래곤 세대 그리기 (배열 복사 후, 역순서로 반시계 방향 회전 후 기존 이어 붙이기)
    while g > 0:
        g -= 1
        copy = dragon[:]
        for idx in range(len(copy)-1,-1,-1):
            new_d = (copy[idx] + 1) % 4
            dragon.append(new_d)
    for dra in dragon:
        nx,ny = x + direction[dra][0], y + direction[dra][1]
        arr[nx][ny] += 1
        x,y = nx,ny

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans += 1
print(ans)