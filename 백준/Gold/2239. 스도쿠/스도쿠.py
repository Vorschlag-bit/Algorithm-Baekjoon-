from sys import stdin as input

arr = []
for _ in range(9):
    arr.append(list(map(int,input.readline().strip())))

# 특정 행,열에 특정 숫자가 사용 가능한지 확인
blank = []

rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0: blank.append((i,j))
        else:
            num = arr[i][j]
            rows[i][num] = True
            cols[j][num] = True


def dfs(idx):
    global blank,arr
    if idx == len(blank):
        for i in range(9):
            print(''.join(map(str,arr[i])))
        exit()
    # 3,4 => 33
    r,c = blank[idx]
    row,col = (r // 3) * 3, (c // 3) * 3
    # r,c에 1-9중 가능한 최소 수를 넣어야 함
    for num in range(1,10):
        if rows[r][num] or cols[c][num]: continue
        # 3 * 3에 해당 숫자 없는지 확인
        flag = True
        for i in range(3):
            if not flag: break
            for j in range(3):
                if arr[row+i][col+j] == num:
                    flag = False
                    break
        
        if not flag: continue
        rows[r][num] = True
        cols[c][num] = True
        arr[r][c] = num
        dfs(idx+1)
        rows[r][num] = False
        cols[c][num] = False
        arr[r][c] = 0

dfs(0)