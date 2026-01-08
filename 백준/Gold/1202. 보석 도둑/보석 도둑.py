from sys import stdin as input
import heapq

n,k = map(int,input.readline().split())

# 각 보석은 무게와 가격
arr = [list(map(int,input.readline().split())) for _ in range(n)]
# 무게 오름차순
arr.sort(key=lambda x: x[0])
# 가방은 담을 수 있는 무게
bag = [int(input.readline()) for _ in range(k)]
# 무게 오름차순
bag.sort()

ans = 0
q = []
idx = 0
# 무게가 작은 가방부터 시작
for i in range(k):
    w = bag[i]
    # w보다 작은 무게의 보석을 모두 heap에 담기
    while idx < len(arr):
        v,c = arr[idx]
        if v <= w:
            heapq.heappush(q,-c)
            idx += 1
        else: break
    if q:
        cost = heapq.heappop(q)
        ans += cost
print(-ans)