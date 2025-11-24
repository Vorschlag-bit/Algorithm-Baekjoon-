from sys import stdin as input

n,m = map(int,input.readline().split())

# [원칙 1] 배열 크기는 반드시 (N+1) * (M+1)로
prefix = [[0] * (m+1) for _ in range(n+1)]

# 원본 데이터와 누적합을 동시에 처리
for i in range(1,n+1):
    arr = list(map(int,input.readline().split()))
    for j in range(1,m+1):
        # [원칙 2] (1,1)부터 채우기 & 2차원 누적합 공식 사용
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[j-1]

k = int(input.readline())

for _ in range(k):
    x1,y1,x2,y2 = map(int,input.readline().split())
    # [원칙 3] 면적합 공식 사용
    # x1,x2,y1,y2에 대한 좌표 보정할 필요 X
    ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(ans)