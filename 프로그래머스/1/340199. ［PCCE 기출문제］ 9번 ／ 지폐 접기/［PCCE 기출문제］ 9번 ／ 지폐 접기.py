def solution(w, b):
    ans = 0
    n,m = b
    tn,tm = w
    while True:
        if n <= tn and m <= tm or n <= tm and m <= tn:
            return ans
        bg = max(n,m)
        sm = min(m,n)
        bg //= 2
        n = bg
        m = sm
        ans += 1
    return ans