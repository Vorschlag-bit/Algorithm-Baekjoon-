from sys import stdin as input

cmd = list(map(int,input.readline().split()))

# 중앙에 있는 발이 움직이면 2
# 인접한 곳 이동이면 3(왼->위/아래, 위->오른/왼)
# 반대편으로 이동하면 4(왼->오른, 위->아래)
# 같은 지점이면 1

# DP
# dp[i][j][k] = i턴에 왼발이 j, 오른발이 k인 상태
dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(len(cmd))]
# 위 = 1, 왼쪽 = 2, 아래 = 3, 오른쪽 = 4, 가운데 = 0
def get_c(cur,nxt):
    # 제자리
    if cur == nxt: return 1
    if cur == 0: return 2
    # 반대
    if (cur+2)%4 == nxt%4: return 4
    # 인접
    else: return 3

dp[0][0][0] = 0
for i in range(len(cmd)-1):
    nxt = cmd[i]
    for r in range(5):
        for l in range(5):
            # 둘 다 같은 발이면 안 됌
            if r != 0 and l != 0 and r == l: continue
            # 해당 스탭이 애초에 불가능한 경우면 pass
            if dp[i][l][r] == float('inf'): continue
            l_c = get_c(l,nxt)
            r_c = get_c(r,nxt)
            # 왼발
            dp[i+1][nxt][r] = min(dp[i][l][r] + l_c, dp[i+1][nxt][r])
            # 오른발
            dp[i+1][l][nxt] = min(dp[i][l][r] + r_c, dp[i+1][l][nxt])

ans = float('inf')
for r in range(5):
    for l in range(5):
        ans = min(ans, dp[len(cmd)-1][r][l])

print(ans)