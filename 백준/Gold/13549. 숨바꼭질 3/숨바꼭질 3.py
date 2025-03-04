from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #출발 / 도착
dist = [0] * 100001 #최대 0부터 100000까지의 지점까지 걸리는 횟수 기록

#BFS 탐색
queue = deque()
queue.append(N) #시작점

# 큐가 빌 때까지 탐색
while queue:
    x = queue.popleft()
    # 도착지점이라면 탐색 종료
    if x == K:
        print(dist[x])
        break

    # x에서 -1 또는 +1 또는 *2 탐색
    for nextX in (x*2, x-1, x+1):
        # 0~100000지점 내이고, 방문하지 않았다면
        if 0 <= nextX <= 100000 and not dist[nextX]:
            if nextX == x*2:
                dist[nextX] = dist[x]
            else:
                dist[nextX] = dist[x] + 1 #방문하고 횟수 1늘림
            queue.append(nextX) #큐에 추가