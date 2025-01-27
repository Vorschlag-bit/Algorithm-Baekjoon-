import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
result = [0] * n
q = deque()

# arr을 n - 1부터 0까지 순회, 큐를 차례로 순회하면서 자기보다 큰 수까지 찾기
for i in range(n - 1, -1, -1):
    while q and q[0] <= arr[i]:
        q.popleft()
    
    if not q:
        result[i] = -1
    else:
        result[i] = q[0]
    q.appendleft(arr[i])
print(*result)