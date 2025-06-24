def gcd(n,m):
    # 두 수의 최대공약수 => 유클리드 호제법
    while m:
        n,m = m,n%m
    return n

def solution(n, m):
    return [gcd(n,m), n*m//gcd(n,m)]