from sys import stdin as input
from collections import deque

arr = list(input.readline().rstrip())
stack = deque()
ans = 0
stick = 0
for char in arr:
    # '(' == char라면 쌓이는 막대기 개수가 증가
    # ')' == char라면 스택[-1]이 '('라면 레이저이므로 ans += stick - 1
    # 스택의[-1]이 ')'라면 stick -= 1
    if char == '(':
        stack.append(char)
        stick += 1
    else:
        if stack[-1] == '(':
            stack.append(char)
            ans += stick - 1
            stick -= 1
        else:
            stack.append(char)
            ans += 1
            stick -= 1
print(ans)

