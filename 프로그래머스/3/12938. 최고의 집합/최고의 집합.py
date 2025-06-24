def solution(n, s):
    ans = []
    # n개의 원소 합이 s면서 곱 최대 => ele 간의 격차 최소화
    # s를 n으로 나누고 부족한 건 n-1에 나눠주기
    if s < n: return [-1]
    q,r = divmod(s,n)
    arr = [q]*n
    for i in range(r):
        arr[i] += 1
    return sorted(arr) if arr else [-1]