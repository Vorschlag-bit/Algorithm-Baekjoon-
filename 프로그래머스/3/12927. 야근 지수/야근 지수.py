import heapq
def solution(n, works):
    if sum(works) <= n: return 0
    # 최대힙을 위해서 -w를 저장하기로
    arr = [-w for w in works]
    heapq.heapify(arr)
    while n > 0:
        job = heapq.heappop(arr)
        if job == 0: break
        job += 1
        n -= 1
        heapq.heappush(arr,job)
    ans = sum(w**2 for w in arr)
    return ans