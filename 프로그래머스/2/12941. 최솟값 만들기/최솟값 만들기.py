import heapq
def solution(A,B):
    ans = 0
    heapq.heapify(A)
    B = [-i for i in B]
    heapq.heapify(B)
    while A:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        ans += a*(-b)
    
    return ans