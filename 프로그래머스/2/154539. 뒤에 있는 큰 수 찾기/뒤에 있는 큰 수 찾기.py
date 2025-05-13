def solution(num):
    stack = []
    l = len(num)
    ans = [-1]*l
    for i in range(l-1,-1,-1):
        while stack and stack[-1] <= num[i]:
            stack.pop()
        if not stack: pass
        else: ans[i] = stack[-1]
        stack.append(num[i])
    return ans