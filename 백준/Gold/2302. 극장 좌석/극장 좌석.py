from sys import stdin as input

# 일반 회원 = 자기 좌석 + 양 옆 좌석 앉기 가능
# vip = 자기 좌석만 가능

n = int(input.readline())
m = int(input.readline())

# 1-based + 1
dp = [0] * (n+2)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] += (dp[i-1] + dp[i-2])

pre = 0
ans = 1
for _ in range(m):
    num = int(input.readline())
    # num - pre로
    i = num - pre - 1
    ans *= dp[i]
    pre = num
# 마지막 배열 수
ans *= dp[n - pre]

print(ans)