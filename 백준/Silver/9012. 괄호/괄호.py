from sys import stdin as input
from collections import deque

n = int(input.readline().rstrip())

for _ in range(n):
    s = input.readline().rstrip()
    stack = deque()
    # 짝을 만나면 pop, 아니면 append
    vps = True
    for char in s:
        if char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                vps = False
                break
        else:
            stack.append(char)
    if stack: vps = False
    print("YES" if vps else "NO")

