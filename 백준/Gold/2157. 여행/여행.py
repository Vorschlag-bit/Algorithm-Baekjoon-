from sys import stdin as input

n,m,k = map(int, input.readline().split())
# 최댓값만 저장할 배열 (i -> j, 경로가 없을 경우 -1)
route = [[-1] * (n+1) for _ in range(n+1)]
# 이동은 번호가 증가하는 방향으로만 해야 함(동 -> 서)
for _ in range(k):
    a,b,c = map(int,input.readline().split())
    # 역방향 무시
    if a > b: continue
    route[a][b] = max(route[a][b], c)    

ans = 0

# a번 도시에서 b번 도시로 이동, c점 점수
# 서 -> 동도 입력 가능(가면 안 됌)
# 같은 도시 쌍에 여러 루트가 존재할 수도 있다. 

# 시작은 반드시 1, 도착은 N, 방문한 도시의 합이 m개 이하여야 한다.
# 필요한 게 중간 과정이 전부 다 인가 아니면 바로 이전 도시만 있으면 되는가
# 비트 마스킹으로 하려면, 300 * 2^300 => 불가능

# dp[i][j] = i번 도시에 도착했을 때 j개의 도시를 방문한 상태의 최댓값
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n):
    for j in range(1,m):
        # i번 도시에서 갈 수 있느 도시에 pushDP로 값을 뿌려주기만 하면 된다
        # 불가능한 조건 pass
        if j > i: continue
        # 1번을 안 거치고 오기
        if i > 1 and j == 1: continue
        for k in range(i+1,n+1):
            # i -> k로 갈 수 있는 방법들
            score = route[i][k]
            # 가는 법 없으면 pass
            if score == -1: continue
            # 중간 길인데 점수가 0이면 안 된다.
            if j > 1 and dp[i][j] == 0: continue
            dp[k][j+1] = max(dp[k][j+1], dp[i][j] + score)

print(max(dp[n]))