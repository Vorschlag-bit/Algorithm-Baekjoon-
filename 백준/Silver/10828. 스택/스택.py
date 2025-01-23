import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n = int(input())
result = []

def stack(command):
    parts = command.split()
    cmd = parts[0]

    if cmd == "push":
        q.append(int(parts[1]))
    elif cmd == "pop":
        if q:
            result.append(int(q.pop()))
        else:
            result.append(-1)
    elif cmd == "size":
        result.append(len(q))
    elif cmd == "empty":
        if not q:
            result.append(1)
        else:
            result.append(0)
    else:
        if q:
            result.append(q[-1])
        else:
            result.append(-1)

for _ in range(n):
    stack(input().strip())

print("\n".join(map(str, result)))
