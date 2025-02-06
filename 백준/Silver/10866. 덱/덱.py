import sys
from collections import deque

q = deque()
input = sys.stdin.readline

commands = []
n = int(input().strip())

for _ in range(n):
    commands.append(input().rstrip())


for cmd in commands:
    if cmd.startswith("push_front"):
        _, num = cmd.split()
        q.appendleft(num)
    elif cmd.startswith("push_back"):
        _, num = cmd.split()
        q.append(num)
    elif cmd == "pop_front":
        print(q.popleft() if q else -1)
    elif cmd == "pop_back":
        print(q.pop() if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "empty":
        print(0 if q else 1)
    else:  # back
        print(q[-1] if q else -1)