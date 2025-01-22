import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n, k = map(int, input().split())

for i in range(1, n + 1):
    q.append(i)
result = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    result.append(str(q.popleft()))
print('<' + ', '.join(result) + '>')