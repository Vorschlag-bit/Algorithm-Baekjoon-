def solution(price, money, cnt):
    p = 0
    for i in range(1,cnt+1):
        p += price * i
    return abs(money-p) if money < p else 0