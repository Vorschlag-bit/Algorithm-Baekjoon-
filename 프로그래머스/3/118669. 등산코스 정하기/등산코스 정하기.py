import heapq
from collections import defaultdict
def solution(n, paths, gates, summits):
    # 봉우리 번호, 최소 inten
    ans = [0,float('inf')]
    # 1-n 번호(출입구,쉼터,봉우리)
    # 그래프(가중치 존재) -> heap
    # 등간 코스 중 inten이 최소가 되는 등산코스
    q = []
    gate = set(gates)
    summit = set(summits)
    graph = defaultdict(list)
    for a,b,w in paths:
        graph[a].append((b,w))
        graph[b].append((a,w))
    # q에 넣을 요소
    # h,cur,visit
    for g in gate:
        heapq.heappush(q,(0,g))
    
    # 해당 노드 최소 inten
    dis = [float('inf')] * (n+1)
    
    while q:
        # 현재까지 최대 inten
        h,cur = heapq.heappop(q)
        if dis[cur] < h: continue
        # cur = 도착지라면 정답과 비교
        if cur in summit:
            if (ans[1] > h or
                (ans[1] == h and ans[0] > cur)):
                ans[1] = h
                ans[0] = cur
            continue
        
        for nxt,w in graph[cur]:
            # 최대 갱신
            til_max = max(w,h)
            # 최대 inten이 아닌 경우 무시
            if dis[nxt] <= til_max: continue
            # 다음 곳이 gate여도 무시
            if nxt in gate: continue
            # 방문 안 한 곳
            dis[nxt] = til_max
            heapq.heappush(q,(til_max,nxt))
    return ans