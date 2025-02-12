from sys import stdin
from collections import deque

while True:
    s = stdin.readline().rstrip()
    if s == '.':
        break
    
    stack = deque()
    error = False
    
    for char in s:
        if char in '([':
            stack.append(char)
        elif char == ']':
            if not stack or stack[-1] != '[':
                error = True
                break
            stack.pop()
        elif char == ')':
            if not stack or stack[-1] != '(':
                error = True
                break
            stack.pop()
            
    if stack: error = True
    print("no" if error else "yes")