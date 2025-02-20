from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 격자 2배
    arr = [[-1] * 102 for _ in range(102)]    
    visit = [[0] * 102 for _ in range(102)]
    ans = 0
    for r in rectangle:
        # 좌표 2배
        x = r[0] * 2
        y = r[1] * 2
        X = r[2] * 2
        Y = r[3] * 2
        for a in range(y, Y + 1):
            for b in range(x, X + 1):
                # 내부면 0으로 초기화
                if x < b < X and y < a < Y:
                    arr[a][b] = 0
                # 내부가 아니면서 다른 사각형에 포함되지 않는다면 1
                elif arr[a][b] != 0:
                    arr[a][b] = 1
        
    def bfs(x, y):
        global ans
        q = deque()
        q.append((x, y))
        visit[y][x] = 1
        while q:
            cx, cy = q.popleft()
            if cx == itemX * 2 and cy == itemY * 2:
                return visit[cy][cx] // 2
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if arr[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[cy][cx] + 1
                    q.append((nx, ny))
            
    return bfs(characterX * 2, characterY * 2)