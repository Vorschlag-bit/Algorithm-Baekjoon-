from sys import stdin as input
from collections import deque,defaultdict
# 특정 건물까지 최소 시간
t = int(input.readline())
ans = []
for _ in range(t):
    # 건물 개수, 규칙 총 개수
    n,k = map(int,input.readline().split())
    # 건물 짓는 쇼요 시간
    time = [0] + list(map(int,input.readline().split()))
    graph = defaultdict(list)
    # x,y -> y가 x 앞에 위치해야 한다
    indegree = [0] * (n+1)
    for _ in range(k):
        x,y = map(int,input.readline().split())
        indegree[y] += 1
        graph[x].append(y)
        # graph[a] = (b,c) -> a로부터 b 노드가 c만큼의 가중치로 떨어져 있음.
    # 목표 건물
    w = int(input.readline())
    q = deque()
    # ingdegree가 0인 거 q에 넣기
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    # 최소의 시간은 i를 지을 수 있는데까지 걸리는 데에 최대 시간 + 해당 소요 시간
    # dp[nxt] = max(dp[nxt], dp[cur] + time[cur])
    dp = [0] * (n+1)
    while q:
        cur = q.popleft()
        if cur == w:
            ans.append(dp[cur] + time[cur])
            break
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[cur] + time[cur])
            if indegree[nxt] == 0:
                q.append(nxt)
print('\n'.join(map(str,ans)))