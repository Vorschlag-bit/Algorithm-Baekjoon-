from sys import stdin as input

n, x = map(int, input.readline().split())
dp = [0 for _ in range(x + 1)]

dp[0] = 1

for _ in range(n):
    l, cnt = map(int, input.readline().split())
    
    # x부터 0까지 역순으로 반복
    for i in range(x, 0, -1):
        # 현재 파이프 길이(개수에 따른)
        cur_l = 0
        for j in range(cnt):
            cur_l += l
            if i - cur_l < 0: break
            dp[i] += dp[i - cur_l]
print(dp[x])