def cnt(n):
    if n == 1: return 0
    m = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a = i
            b = n // i
            if b <= 10**7: return b
            if a <= 10**7: m = max(m,a)
    return m
def solution(begin, end):
    ans = []
    # 최대 길이 10억(1-based)
    # 특정 수 n에 대해서 n에 적힐 숫자를 알아보자
    # 10 <- 10의 약수 중 가장 큰 수가 들어간다. 최대약수
    for n in range(begin,end+1):
        ans.append(cnt(n))
    return ans