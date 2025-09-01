from sys import stdin as input

n = int(input.readline())
arr = [[0] * 10 for _ in range(10)]
cmd = []
for _ in range(n):
    t,x,y = map(int,input.readline().split())
    cmd.append((t,x,y))
ans = 0

def move_green(t,x,y):
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
        while r + 1 < 10 and arr[r+1][y] == 0:
            r += 1
        arr[r][y] = 1
        arr[r-1][y] = 1

def move_blue(t,x,y):
    c = y
    if t == 1:
        while c + 1 < 10 and arr[x][c+1] == 0:
            c += 1
        arr[x][c] = 1
    elif t == 2:
        while c + 1 < 10 and arr[x][c+1] == 0:
            c += 1
        arr[x][c] = 1
        arr[x][c-1] = 1
    else:
        while c + 1 < 10 and arr[x+1][c+1] == 0 and arr[x][c+1] == 0:
            c += 1
        arr[x][c] = 1
        arr[x+1][c] = 1

def combo_green():
    global ans
    for i in range(6,10):
        if sum(arr[i][:4]) == 4:
            ans += 1
            for j in range(4): arr[i][j] = 0
            for row in range(i-1,-1,-1):
                for j in range(4):
                    arr[row+1][j] = arr[row][j]
                    arr[row][j] = 0

def combo_blue():
    global ans
    for j in range(6,10):
        cnt = 0
        for i in range(4):
            if arr[i][j] == 1: cnt += 1
        if cnt == 4:
            ans += 1
            for i in range(4): arr[i][j] = 0
            for col in range(j-1,-1,-1):
                for i in range(4):
                    arr[i][col+1] = arr[i][col]
                    arr[i][col] = 0

def light_green():
    # row 4,5
    l = []
    for r in [4,5]:
        if sum(arr[r][:4]) > 0: l.append(r)
    if len(l) == 0: return

    for i in range(9,-1,-1):
        nxt = i + len(l)
        if nxt < 10:
            for j in range(4):
                arr[nxt][j] = arr[i][j]
    
    for r in l:
        for j in range(4):
            arr[r][j] = 0

def light_blue():
    # col 4,5
    l = []
    for c in [4,5]:
        cnt = 0
        for i in range(4):
            if arr[i][c] > 0: cnt += 1
        if cnt > 0: l.append(c)
    
    if len(l) == 0: return

    for j in range(9,-1,-1):
        nxt = j + len(l)
        if nxt < 10:
            for i in range(4):
                arr[i][nxt] = arr[i][j]
    
    for c in l:
        for i in range(4):
            arr[i][c] = 0
    
for com in cmd:
    t,x,y = com
    move_green(t,x,y)
    move_blue(t,x,y)

    combo_green()
    combo_blue()

    light_green()
    light_blue()

count = 0
for i in range(6,10):
    for j in range(4):
        if arr[i][j] == 1: count += 1

for j in range(6,10):
    for i in range(4):
        if arr[i][j] == 1: count += 1
print(ans)
print(count)