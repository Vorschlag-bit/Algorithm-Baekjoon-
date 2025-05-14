import heapq
def solution(n, k, enemy):
    q = []
    for i,e in enumerate(enemy):
        n -= e
        # maxheap을 사용해서, 최대의 병사 공격 순으로 트리 생성
        heapq.heappush(q,-e)
        if n < 0:
                if k > 0:
                    max_v = -heapq.heappop(q)
                    n += max_v
                    k -= 1
                # 더이상 막을 수 없다면
                else: return i
    return len(enemy)