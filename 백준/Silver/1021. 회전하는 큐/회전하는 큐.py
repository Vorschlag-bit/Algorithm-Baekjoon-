import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
dq = deque([i for i in range(1, n + 1)])
ans = 0

for i in arr:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    ans += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop()) 
                    ans += 1
print(ans)