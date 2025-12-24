from sys import stdin as input

c,n = map(int,input.readline().split())

cost = [0] * n
l = 0
for i in range(n):
    # 홍보 비용, 얻을 수 있는 고객 수
    co,cos = map(int,input.readline().split())
    l = max(l,cos)
    cost[i] = (co,cos)
cost.sort(key=lambda x: x[0])
# 적어도 c명 얻기 위해 사용할 최소 비용 출력 -> 조합
# 도시별로 모두 다 차곡차곡 쌓아보기
# dp[n] = n명 얻기 위한 최소 비용
dp = [float('inf')] * (c+l+1)
dp[0] = 0
ans = float('inf')
for i in range(n):
    # 홍보 비용, 얻을 수 있는 고객 수
    bill,cos_n = cost[i]
    for j in range(cos_n,len(dp)):
        dp[j] = min(dp[j], dp[j-cos_n] + bill)
        if j >= c:
            ans = min(ans,dp[j])
print(ans)