from sys import stdin as input
from collections import deque
n,t = map(int,input.readline().split())

q = deque()

q.append((n,0))
visit = set()
visit.add(n)
while q:
    cur,v = q.popleft()
    if cur * 2 <= t:
        if cur*2 not in visit:
            visit.add(cur*2)
            if cur * 2 == t:
                print(v+2)
                exit()
            q.append((cur*2,v+1))
    if cur * 10 + 1 <= t:
        if cur*10+1 not in visit:
            visit.add(cur*10+1)
            if cur * 10 + 1 == t:
                print(v+2)
                exit()
            q.append((cur*10+1,v+1))
print(-1)