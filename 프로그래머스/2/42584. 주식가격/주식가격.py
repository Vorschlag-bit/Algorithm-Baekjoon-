def solution(prices):
    stack = []
    ans = [0]*len(prices)
    # pop되는 순간이 떨어지는 시간
    for i,p in enumerate(prices):
        while stack and stack[-1][1] > p:
            idx,pr = stack.pop()
            ans[idx] = i-idx
        stack.append((i,p))
    while stack:
        idx,pr = stack.pop()
        ans[idx] = len(prices)-idx-1
    return ans