def solution(n):
    n = str(n)
    n = sorted(n,reverse=True)
    answer = ''
    for i in n:
        answer += i
    return int(answer)