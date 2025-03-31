n, m, h = map(int, input().split())
arr = [[0] * n for _ in range(h)]
# arr[r][c] == 1 -> r번째 줄의 c와 c+1 세로줄을 연결하는 가로줄이 있음
ans = 4
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

def check(arr):
    # 각 세로 선이 자기 번호로 도착하는지 확인
    for i in range(n):
        p = i  # 현재 위치
        # 각 높이마다 확인
        for j in range(h):
            # 현재 위치에서 오른쪽으로 이동 가능한 경우
            if p < n-1 and arr[j][p] == 1:
                p += 1
            # 현재 위치에서 왼쪽으로 이동 가능한 경우
            elif p > 0 and arr[j][p-1] == 1:
                p -= 1
        # 모든 높이를 지난 후 원래 번호로 돌아오지 않으면 실패
        if p != i:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    
    # 이미 찾은 최소값보다 많은 사다리를 놓았거나, 3개 이상이면 종료
    if cnt >= ans:
        return
    
    # 사다리 결과 체크
    if check(arr):
        ans = min(ans, cnt)
        return
    
    # 3개 이상의 사다리를 추가해야 한다면 종료
    if cnt == 3:
        return
    
    # 사다리 추가하기
    for r in range(x, h):
        k = y if r == x else 0  # 같은 행이면 이전 열부터 시작
        for c in range(k, n-1):
            # 현재 위치와 양옆에 사다리가 없는 경우만 추가 가능
            if arr[r][c] == 0:
                if c > 0 and arr[r][c-1] == 1:  # 왼쪽에 사다리가 있는지 확인
                    continue
                if c < n-2 and arr[r][c+1] == 1:  # 오른쪽에 사다리가 있는지 확인
                    continue
                
                arr[r][c] = 1  # 사다리 추가
                # 다음 탐색 - 같은 위치에 연속해서 사다리를 놓을 수 없으므로 c+1부터 시작
                dfs(cnt+1, r, c+2)
                arr[r][c] = 0  # 사다리 제거(백트래킹)

dfs(0, 0, 0)
print(ans if ans < 4 else -1)