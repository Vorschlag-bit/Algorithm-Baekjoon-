import heapq
def solution(scov, K):
    answer = 0
    q = []
    for s in scov:
        heapq.heappush(q,s)
    while True:
        s = q[0]
        if s >= K:
            break
        if len(q) == 1:
            return -1
        heapq.heappop(q)
        second = heapq.heappop(q)
        new = s + (second * 2)
        answer += 1
        heapq.heappush(q,new)
    return answer