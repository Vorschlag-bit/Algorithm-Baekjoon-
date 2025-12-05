from sys import stdin as input

n,m = map(int,input.readline().split())
inf = -float('inf')
arr = [0]

for _ in range(n):
    arr.append(int(input.readline()))

# 누적합으로 미리 계산(특정 지점 i,j에 대한 구간합 = arr[j] - arr[i])
for i in range(1,len(arr)):
    arr[i] += arr[i-1]

# dp[i][j] i까지의 인덱스 기준, j개의 구간에 속한 수들의 총 합
dp = [[inf] * (m+1) for _ in range(n+1)]
for j in range(n+1):
    dp[j][0] = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        # i까지 봤을 때, j개의 구간이 생겨야 함.
        # 1 -> 1, 2 -> 1,2,3, 3-> 1,2,3,4,5
        if i < 2*j - 1: continue
        # 1. j개의 구간에 i가 포함 안 되는 경우: 
        dp[i][j] = dp[i-1][j]
        # 2. i가 j번째 구간에 포함되는 경우: [k,i]
        # k-2 지점까지 j-1개의 구간이 있어야 한다.
        for k in range(1, i+1):
            if k >= 2:
                prev = dp[k-2][j-1]
            # 그 구간이 처음일 경우
            else:
                # 1개의 구간에서 최댓값을 보려고 하면 이전은 0
                if j == 1:
                    prev = 0
                # 마지막 구간의 시작이 1인데 2개 이상의 구간을 보는 건 불가능
                else:
                    prev = inf
            if prev != inf:
                dp[i][j] = max(dp[i][j], prev + arr[i] - arr[k-1])

print(dp[n][m])