from sys import stdin as input

n = int(input.readline().strip())

cur = input.readline().strip()

pwd = input.readline().strip()

# 자물쇠의 디스크를 최대 3칸 시계,반시계로 돌릴 수 있음
# 인접한 3개의 디스크를 한 번에 돌릴 수 있음
# 최대 100의 자리수
# 과정의 모든 수가 필요 -> 하지만 on/off의 문제가 아니므로 비트 마스킹은 불가능
# dp[i][j][k] = i: 현재 돌리려는 수의 인덱스, j: i-2,i-1의 돌림으로 영향을 받은 i의 회전 수, k: i-1로 영향을 받은 i+1의 회전 수
# pushDp -> 영향을 줘야 함
# 1. 1칸으로 gap
# dp[i][j][k] = 
dp = [[[float('inf')] * 10 for _ in range(10)] for _ in range(n+1)]
dp[0][0][0] = 0
COST = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1]
for i in range(n):
    for j in range(10):
        for k in range(10):
            if dp[i][j][k] == float('inf'): continue
            # 최소 회전 횟수
            # gap은 j(i-1, i-2)의 회전 횟수에 영향을 받는다.
            cur_val = (int(cur[i]) + j) % 10
            gap = (int(pwd[i]) - cur_val + 10) % 10
            # three: 3칸짜리 회전량 (i, i+1, i+2 영향)
            # two: 2칸짜리 회전량 (i, i+1 영향)
            for three in range(10):
                for two in range(10):
                    # one: 1칸짜리 회전량 (i만 영향)
                    # i번째 자물쇠는 (one + two + three) 만큼 돌아가서 gap이 되어야 함
                    one = (gap - three - two) % 10
                    
                    # 최소 비용
                    cost = COST[one] + COST[two] + COST[three]

                    # 상태전이
                    # 1. i+1는 기존의 k에서 x + y만큼 이동
                    nxt_j = (k + two + three) % 10
                    # 2. i+2는 기존의 k에서 y만큼 이동
                    nxt_k = three
                    dp[i+1][nxt_j][nxt_k] = min(dp[i+1][nxt_j][nxt_k], dp[i][j][k] + cost)

print(dp[n][0][0])