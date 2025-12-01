n = input()

# n이 주어질 때, 그 암호의 해석이 몇 가지 나올 수 있는지 출력
# 마지막 i기준, i를 1자리로 해석할 경우 (1~9)
# dp[i] += dp[i-1] + dp[i-2]
# i를 2자리로 해석이 가능할 경우 (11 ~ 26)
# dp[i] += dp[i-2]

if n == "0":
    print(0)
    exit()

n = "0" + n

dp = [0] * len(n)
dp[0] = 1

for i in range(1,len(n)):
    cur = n[i]
    pre = n[i-1]
    # 1자리로 해석(현재 자리가 0이 아녀야 함)
    if cur != "0":
        dp[i] += dp[i-1]
    # 2자리로 해석(이전 + 현재가 10 <= s <= 26일 경우)
    num = int(pre + cur)
    if 10 <= num <= 26:
        dp[i] += dp[i-2]

print(dp[len(n)-1]%1000000)