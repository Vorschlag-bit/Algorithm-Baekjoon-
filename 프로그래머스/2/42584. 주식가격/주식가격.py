def solution(prices):
    stack = []
    arr = []
    # pop되는 순간이 떨어지는 시간
    for i,p in enumerate(prices):
        while stack and stack[-1][1] > p:
            idx,pr = stack.pop()
            arr.append((idx,i-idx))
        stack.append((i,p))
    while stack:
        idx,pr = stack.pop()
        arr.append((idx,len(prices)-idx-1))
    arr.sort(key=lambda x: x[0])
    return [arr[i][1] for i in range(len(prices))]