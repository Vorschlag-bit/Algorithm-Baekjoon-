def solution(number, k):
    stack = []
    for n in number:
        n = int(n)
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0:
        stack = stack[:-k]
    return "".join(list(map(str,stack)))