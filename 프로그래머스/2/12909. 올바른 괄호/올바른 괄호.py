def solution(s):
    ans = True
    stack = []
    for e in s:
        if e == '(':
            stack.append(e)
        else:
            if not stack or stack[-1] != '(':
                ans = False
                break
            else: stack.pop()
    if stack: ans = False
    return ans