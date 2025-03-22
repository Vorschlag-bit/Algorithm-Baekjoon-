def solution(cap, n, d, p):
    answer = 0
    for i in range(n-2,-1,-1):
        d[i] += d[i+1]
        p[i] += p[i+1]
    t = 0
    for i in range(n-1,-1,-1):
        while d[i] > cap*t or p[i] > cap*t:
            answer += (i+1)*2
            t += 1
    return answer