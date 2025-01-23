import sys
from collections import deque

q = deque()
input = sys.stdin.readline

n = int(input())
flag = True
result = []
top = 1
for _ in range(n):
    num = int(input())
    while top <= num:
        q.append(top)
        result.append('+')
        top += 1
    if q and q[-1] == num:
        q.pop()
        result.append('-')
    else:
        flag = False
        break
print("\n".join(result) if flag else "NO")