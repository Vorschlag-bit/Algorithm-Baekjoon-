# 경찰차 1은 (1,1), 2는 (n,n)에서 시작
# 연락받은 경찰차는 최단 거리로 이동하고, 거기서 대기
# 사건 발생 순서대로 경찰차에게 맡김. 두 경찰차의 이동 거리의 최솟값을 구하기
from sys import stdin as input
n = int(input.readline())
t = int(input.readline())
p1 = [(1,1)]
p2 = [(n,n)]
# 1-based
for _ in range(t):
    r,c = map(int,input.readline().split())
    p1.append((r,c))
    p2.append((r,c))
# dp[i][j] = 경찰차1이 맡은 마지막 사건이 i번이고, 경찰차2가 맡은 마지막 사건이 j번일 경우 최소 거리의 합
dp = [[float('inf')] * (t+1) for _ in range(t+1)]
dp[0][0] = 0

# 추적용 배열 = (i,j)에 오기전 (pre_i,pre_j)를 저장
trace = [[None] * (t+1) for _ in range(t+1)]

for i in range(t):
    for j in range(t):
        # 다음 사건은 i,j 중 더 큰 거 + 1
        nxt = max(i,j) + 1
        # 경찰차 1
        cr,cc = p1[i]
        nr,nc = p1[nxt]
        # 경찰차 1이 nxt번을 맡으려면 i,j에서 옮겨와야 함
        d1 = abs(cr - nr) + abs(cc - nc)
        if d1 + dp[i][j] < dp[nxt][j]:
            # nxt번에 대한 trace 추가
            trace[nxt][j] = (i,j)
            dp[nxt][j] = d1 + dp[i][j]
        # 경찰차 2
        cr,cc = p2[j]
        d2 = abs(cr - nr) + abs(cc - nc)
        if d2 + dp[i][j] < dp[i][nxt]:
            trace[i][nxt] = (i,j)
            dp[i][nxt] = d2 + dp[i][j]
ans = float('inf')
end_i,end_j = -1,-1
for i in range(t):
    if ans > dp[t][i]:
        end_i,end_j = t,i
        ans = dp[t][i]
    if ans > dp[i][t]:
        end_i,end_j = i,t
        ans = dp[i][t]
print(ans)

# end_i,end_j로부터 타고 올라가기
path = []
while True:
    if end_i == 0 and end_j == 0: break
    pre_i,pre_j = trace[end_i][end_j]
    # j가 증가했다 => 2번
    if pre_j < end_j:
        path.append(2)
    # 아니면 1번
    else:
        path.append(1)
    end_i,end_j = pre_i,pre_j

for p in path[::-1]:
    print(p)