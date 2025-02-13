from sys import stdin as input
from collections import deque

n = int(input.readline().rstrip())
ans = 0

for _ in range(n):
    s = input.readline().rstrip()
    stack = deque()
    good = True
    for char in s:
        # char가 A인 경우
        if char == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(char)
        # B인 경우
        else:
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(char)
    if not stack: ans += 1
print(ans)

