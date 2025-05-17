def solution(order):
    ans = 0
    # lifo(stack)
    # 4,3,6,5,2,1 -> 1,2,3,4
    stack = []
    # 4가 -1이 될 때까지 push
    cnt = 1
    for o in order:
        while cnt <= o:
            stack.append(cnt)
            cnt += 1
        if stack and stack[-1] == o:
            stack.pop()
            ans += 1
        else: break
    return ans