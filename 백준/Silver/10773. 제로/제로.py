import sys
from collections import deque

q = deque()
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        q.pop()
    else:
        q.append(num)

print(sum(q))