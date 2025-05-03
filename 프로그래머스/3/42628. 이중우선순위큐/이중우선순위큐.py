import heapq
def solution(ops):
    maxq = []
    minq = []
    cnt = [0] * 1000001
    for i,op in enumerate(ops):
        cmd,n = op.split()
        n = int(n)
        if cmd =='I':
            heapq.heappush(maxq,-n)
            heapq.heappush(minq,n)
            cnt[n] += 1
        else:
            # 최댓값 삭제
            if n > 0:
                while maxq:
                    v = -heapq.heappop(maxq)
                    if cnt[v] > 0:
                        cnt[v] -= 1
                        break
            # 최솟값 삭제
            else:
                while minq:
                    v = heapq.heappop(minq)
                    if cnt[v] > 0:
                        cnt[v] -= 1
                        break
    minA,maxA = None,None
    while minq:
        v = heapq.heappop(minq)
        if cnt[v] > 0:
            minA = v
            break
    while maxq:
        v = -heapq.heappop(maxq)
        if cnt[v] > 0:
            maxA = v
            break
    if maxA is None or minA is None:
        return [0,0]
    return [maxA,minA]