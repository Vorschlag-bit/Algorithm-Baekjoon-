from collections import deque
def solution(board):
    # 3차원배열 arr[4][n][n]으로 수정
    # 배열의 1번째에는 이전 지점으로부터 남, 서, 북, 동에서 도달했을 때의 최솟값을 저장
    # ex) 이전이 남방향일 경우, 서, 동은 + 500, 남은 + 100
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    M = float('inf')
    n = len(board)
    # 방문 배열을 모두 최댓값으로 초기화
    arr = [[[M for _ in range(n)] for _ in range(n)] for _ in range(4)]
    arr[0][0][0] = 0
    arr[3][0][0] = 0
# 코너가 만들어지는 경우:
# 0(s) -> 1(w), 0(s) -> 3(e)
# 1(w) -> 0(s), 1(w) -> 2(n)
# => d % 2 == 0이라면(남, 북) if 다음 방향이 i % 2 == 1일 경우 500원 발생
# => d % 2 == 1이라면(동, 서) if 다음 방향이 i % 2 == 0일 경우 500원 발생
    def check(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def bfs():
        q = deque()
        # 동, 남 방향으로 
        q.append((0, 0, 0))
        q.append((3, 0, 0))
        while q:
            cd, cx, cy = q.popleft()
            if cx == n - 1 and cy == n - 1: continue
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if not check(nx, ny): continue
                # 다음 값 계산
                # 직진한 경우라면 100 +
                nd = arr[cd][cx][cy]
                if cd % 2 == i % 2:
                    nd += 100
                # 코너링이면 600 +
                else:
                    nd += 600
                
                # bfs 조건: 벽이 아니고, 해당 배열을 특정방향으로 방문했을 때 
                # 더 저렴하다면 재방문
                if board[nx][ny] != 1 and nd < arr[i][nx][ny]:
                    arr[i][nx][ny] = nd
                    q.append((i, nx, ny))
        
    ans = M
    bfs()
    for i in range(4):
        if arr[i][n - 1][n - 1] < ans:
            ans = arr[i][n - 1][n - 1]
    return ans