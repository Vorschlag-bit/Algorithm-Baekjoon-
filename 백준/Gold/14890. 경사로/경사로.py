n,l = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def check_row(r):
# 행 검사
    helper = []
    for i in range(n-1):
        # 현재 열이 더 높을 경우
        if arr[r][i] > arr[r][i+1]:
            h = arr[r][i+1]
            if arr[r][i] - h > 1: return 0
            # i+l이 유효한지 확인
            if i+l > n-1: return 0
            for j in range(i+1,i+l+1):
                if arr[r][j] != h : return 0
                if j in helper: return 0
                helper.append(j)
        # 현재 열이 더 낮은 경우
        elif arr[r][i] < arr[r][i+1]:
            h = arr[r][i]
            if arr[r][i+1] - h > 1: return 0
            if i-l+1 < 0: return 0
            for j in range(i-l+1,i+1):
                if arr[r][j] != h: return 0
                if j in helper: return 0
                helper.append(j)
    return 1

def check_col(c):
# 열 검사
    helper = []
    for i in range(n-1):
        # 현재 행이 더 높을 경우
        if arr[i][c] > arr[i+1][c]:
            # 다음 행 + l만큼 경사로 설치할 수 있는지 확인
            # 0. 높이 차가 1인지 확인
            h = arr[i+1][c]
            if arr[i][c] - h > 1: return 0
            # 1. i+l이 유효한지 확인
            if i+l > n-1: return 0
            # 2. i+l까지 모두 높이가 같은지 확인
            for j in range(i+1,i+1+l):
                if arr[j][c] != h: return 0
            # 3. i+l이 이미 기존 helper에 있는지 확인
                if j in helper: return 0
                helper.append(j)
        # 현재 행이 더 낮을 경우
        elif arr[i][c] < arr[i+1][c]:
            h = arr[i][c]
            if arr[i+1][c] - h > 1: return 0
            if i-l+1 < 0: return 0
            for j in range(i-l+1,i+1):
                if arr[j][c] != h: return 0
                if j in helper: return 0
                helper.append(j)
    return 1


for i in range(n):
    ans += check_row(i)
    ans += check_col(i)
print(ans)