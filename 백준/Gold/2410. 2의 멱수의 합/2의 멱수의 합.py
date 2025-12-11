from sys import stdin as input

n = int(input.readline())

dp = [0] * (n+1)
dp[0] = 1
i = 0
while 2**i <= n:
    # 2의 멱수(1,2,4...)
    cur = 2**i
    # cur로 만들 수 있는 모든 경우의 수 더해주기
    for j in range(cur,n+1):
        dp[j] += dp[j-cur]
    i += 1

print(dp[n] % 1000000000)