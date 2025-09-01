from sys import stdin as input

n = int(input.readline())
arr = [[0] * 10 for _ in range(10)]
cmd = []
for _ in range(n):
    t,x,y = map(int,input.readline().split())
    cmd.append((t,x,y))
ans = 0

def drop_green(t,x,y):
    r = x
    if t == 1:
        while r + 1 < 10 and arr[r+1][y] == 0:
            r += 1
        arr[r][y] = 1
    elif t == 2:
        while r + 1 < 10 and arr[r+1][y] == 0 and arr[r+1][y+1] == 0:
            r += 1
        arr[r][y] = 1
        arr[r][y+1] = 1
    else:
        while r + 1 < 10 and arr[r+1][y] == 0 and arr[r][y] == 0:
            r += 1
        arr[r][y] = 1
        arr[r-1][y] = 1

def drop_blue(t,x,y):
    if t == 1:
        c = y
        while c+1 < 10 and arr[x][c+1] == 0:
            c += 1
        arr[x][c] = 1
    elif t == 2:  # 1×2 가로 → 2×1 세로로 회전
        c = y
        while c+1 < 10 and arr[x][c+1] == 0:
            c += 1
        arr[x][c] = arr[x][c-1] = 1
    else:  # t == 3, 2×1 세로 → 1×2 가로로 회전
        c = y
        while c+1 < 10 and arr[x][c+1] == 0 and arr[x+1][c+1] == 0:
            c += 1
        arr[x][c] = arr[x+1][c] = 1

def combo_green():
    global ans
    for i in range(6,10):
        if sum(arr[i][:4]) == 4:
            ans += 1
            for j in range(4): arr[i][j] = 0
            # 중력이 아니라 해당 0에서 i까지 한 칸씩만 내려오면 된다.
            for row in range(i-1,-1,-1):
                for j in range(4):
                    arr[row+1][j] = arr[row][j]
                    arr[row][j] = 0
    
    return

def combo_blue():
    global ans
    for j in range(6,10):
        cnt = 0
        for i in range(4):
            if arr[i][j] == 1: 
                cnt += 1
        if cnt == 4:
            ans += 1
            for i in range(4): arr[i][j] = 0
            for col in range(j-1,-1,-1):
                for i in range(4):
                    arr[i][col+1] = arr[i][col]
                    arr[i][col] = 0
                
    return

def light_green():
    # 4,5행에서 넘어선 칸 있는지 확인
    cnt = []
    for i in [4,5]:
        if sum(arr[i][:4]) > 0: 
            cnt.append(i)
    if len(cnt) == 0: 
        return
    
    # 아래로 슬라이딩
    for i in range(9,-1,-1):
        nx = i + len(cnt)
        if nx < 10:
            for j in range(4):
                arr[nx][j] = arr[i][j]
                arr[i][j] = 0
    
    # 연한 칸 지우기
    for i in cnt:
        for j in range(4): 
            arr[i][j] = 0

def light_blue():
    # 4,5열에서 넘어선 칸 있는지 확인
    cnt = []
    for j in [4,5]:
        s = 0
        for i in range(4):
            if arr[i][j] == 1: 
                s += 1
        if s > 0: 
            cnt.append(j)
    
    if len(cnt) == 0: 
        return
    
    # 오른쪽으로 슬라이딩
    for j in range(9,-1,-1):
        ny = j + len(cnt)
        if ny < 10:
            for i in range(4):
                arr[i][ny] = arr[i][j]
                arr[i][j] = 0
    
    # 연한 칸 지우기
    for j in cnt:
        for i in range(4): 
            arr[i][j] = 0

for t,x,y in cmd:
    drop_green(t,x,y)
    drop_blue(t,x,y)
    
    combo_green()
    combo_blue()

    
    # 3. 연한 구역 처리
    light_green()
    light_blue()

# 결과 계산
total = 0
for i in range(6,10):
    for j in range(4):
        if arr[i][j] == 1: 
            total += 1
for j in range(6,10):
    for i in range(4):
        if arr[i][j] == 1: 
            total += 1

print(ans)
print(total)