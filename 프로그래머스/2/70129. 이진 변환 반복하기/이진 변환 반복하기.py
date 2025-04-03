def solution(s):
    zero = 0
    t = 0
    while len(s) > 1:
        cnt = sum(1 for i in s if i == '0')
        zero += cnt
        non_zero = s.replace('0','')
        target = len(non_zero)
        s = bin(target)[2:]
        t += 1
    return [t,zero]