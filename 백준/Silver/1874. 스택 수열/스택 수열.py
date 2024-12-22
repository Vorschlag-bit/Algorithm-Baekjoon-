import sys;
from collections import deque;

dq = deque()

arr = []
flag = True
n = int(sys.stdin.readline().strip())

idx = 1
for i in range(n):
    num = int(sys.stdin.readline().strip())

    while idx <= num:
        dq.append(idx)
        arr.append('+')
        idx += 1
    
    if dq[-1] != num:
        flag = False
        break

    dq.pop()
    arr.append('-')

print('\n'.join(arr) if flag else "NO")


