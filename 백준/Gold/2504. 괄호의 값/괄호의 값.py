from sys import stdin as input
from collections import deque

stack = deque()
s = input.readline().rstrip()
right = True
ans = 0
g = 1
before = ''

for char in s:
    if char == '(':
        g *= 2
        stack.append(char)
    elif char == '[':
        g *= 3
        stack.append(char)
    elif char == ')':
        # 스택이 비어있거나 짝이 맞지 않는 경우
        if not stack or stack[-1] != '(':
            right = False
            break
        if before == '(':
            ans += g
        stack.pop()
        g //= 2
    else:
        if not stack or stack[-1] != '[':
            right = False
            break
        if before == '[':
            ans += g
        stack.pop()
        g //= 3
    before = char

if stack:
    right = False
print(ans if right else 0)