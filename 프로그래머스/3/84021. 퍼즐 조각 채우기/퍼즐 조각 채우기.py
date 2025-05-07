from collections import deque,defaultdict
def normalize(t):
    minx = min(x for x,y in t)
    miny = min(y for x,y in t)
    return sorted([(x-minx,y-miny) for x,y in t])

def rotate(arr):
    return [(y,-x) for (x,y) in arr]

def solution(board, table):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    # 조각은 한 번에 하나, 회전 가능, 뒤집기 불가능
    # 퍼즐의 칸 수와 채우려는 빈 칸의 개수가 일치해야 함
    # 일치한다면 모든 빈 칸에 대해서 퍼즐의 모양으로 dfs * 4?(회전)
    # 퍼즐과 빈 칸은 위치가 제각각이므로 상대좌표로 정규화 (0,0) 기준
    n = len(board)
    puzzle = defaultdict(list)
    blank = defaultdict(list)
    def bfs(x,y,p,t):
        nonlocal blank,puzzle
        q = deque()
        q.append((x,y))
        if t == 0: board[x][y] = p
        else: table[x][y] = p
        # 퍼즐/빈칸의 크기
        size = 1
        # 퍼즐/빈칸의 정규화된 좌표
        arr = []
        arr.append((x,y))
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx+direction[i][0],cy+direction[i][1]
                if t == 0:
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = p
                        size += 1
                        arr.append((nx,ny))
                        q.append((nx,ny))
                else:
                    if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == 1:
                        table[nx][ny] = p
                        size += 1
                        arr.append((nx,ny))
                        q.append((nx,ny))
        if t == 0:
            blank[size].append(arr)
        else: puzzle[size].append(arr)
    cnt = 2
    # 빈 칸
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                bfs(i,j,cnt,0)
                cnt += 1
    cnt = 2
    # 퍼즐
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                bfs(i,j,cnt,1)
                cnt += 1
    ans = 0
    for size in blank:
        if size not in puzzle:
            continue
        # 퍼즐 사이즈의 개수
        used = [False]*len(puzzle[size])
        for b_shape in blank[size]:
            shape = normalize(b_shape)
            flag = False
            for idx,p in enumerate(puzzle[size]):
                if used[idx]: continue
                temp = p
                for _ in range(4):
                    temp = rotate(temp)
                    temp = normalize(temp)
                    if shape == temp:
                        flag = True
                        used[idx] = True
                        ans += size
                        break
                if flag: break
    return ans