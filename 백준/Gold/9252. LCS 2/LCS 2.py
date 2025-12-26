from sys import stdin as input

# 첫 번쨰 줄에 lcs 길이
# 두 번째 줄에 lcs 자체
# dp[i][j] = lcs(i,j) -> max(dp[i][j], dp[i][j-1])
a = input.readline().strip()
b = input.readline().strip()
n = len(a)
m = len(b)
dp = [[0] * (m+1) for _ in range(n+1)]

ans = ''
# 역추적  1 = i-1,j-1, 2 = i-1, 3 = j-1

for i in range(1,n+1):
    for j in range(1,m+1):
        # 서로 같을 경우
        if a[i-1] == b[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[n][m])
while n > 0 and m > 0:
    if a[n-1] == b[m-1]:
        ans += a[n-1]
        n -= 1
        m -= 1
    else:
        # 위쪽이랑 같은 경우
        if dp[n][m] == dp[n-1][m]:
            n -= 1
        # 왼쪽이랑 같은 경우
        else:
            m -= 1
print(ans[::-1]) 