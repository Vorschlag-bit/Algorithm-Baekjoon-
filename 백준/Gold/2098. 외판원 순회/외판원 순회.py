from sys import stdin as input

n = int(input.readline())

# 1 ~ N번까지의 도시가 있고, 한 도시에서 출발해 모든 도시를 중복없이 방문하고 다시 처음 도시로 돌아오는 경우의 수
# w[i][j] = i -> j의 비용(i -> j와 j -> i는 다를 수 있음, i -> i는 항상 0, i -> j가 불가능한 경우 비용은 0)

cost = []

for _ in range(n):
    cost.append(list(map(int,input.readline().split())))

b = 2**n
# 비트마스킹으로 지금까지 방문한 도시들을 체크해야 함
# dp[i][j] = i도시에 j 비트 상황으로 방문했을 때 경우의 수
dp = [[float('inf')] * b for _ in range(n)]

# 0에서 출발하는 비용
dp[0][1] = 0

ans = float('inf')
# 가장 적은 방문 도시 상태 -> 가장 많은 도시 방문 상태로 
for bit in range(1,2**n):
    for i in range(n):
        # dp[i][bit] = inf면 pass (아직 도달할 수 없는 상태에서 시작 불가)
        # 현재 방문한 도시 i가 비트에 포함되어 있어야 함
        if bit & (1 << i) == 0: continue
        if dp[i][bit] == float('inf'): continue
        for j in range(n):
            # i -> j의 비용이 0이면 pass
            if i != j and cost[i][j] == 0: continue
            # 다시 방문한 도시 재방문 불가
            if bit & (1 << j): continue
            # 다음 여행의 총 비용
            c = dp[i][bit] + cost[i][j]
            # 다음 여행지 포함한 비트
            nxt = bit | (1 << j)
            if dp[j][nxt] > c:
                dp[j][nxt] = c

for i in range(n):
    if dp[i][b-1] > 0:
        # 다시 0으로 돌아가는 비용이 0이면 pass
        if cost[i][0] == 0: continue
        total = dp[i][b-1] + cost[i][0]
        ans = min(ans, total)

print(ans)