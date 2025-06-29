def solution(x):
    n = sum(int(c) for c in str(x))
    return x % n == 0