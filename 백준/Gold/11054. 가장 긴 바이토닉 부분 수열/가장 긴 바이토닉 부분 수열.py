from sys import stdin as input

n = int(input.readline())

arr = list(map(int,input.readline().split()))

# lis 2개 섞어쓰기
# dp[i]가 곧 최정상의 k(k 미만은 전부 값이 작은 거)
# 정방향
dp1 = [1] * n
# 역방향
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
ans = 0
for i in range(n):
    ans = max(ans, dp1[i] + dp2[i])
# 중복된 k 하나 빼기
print(ans-1)