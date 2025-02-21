n, r, c = map(int, input().split())

def z(i, j, size):
    # size = 0일 경우(baseline)
    if size == 0:
        return 0
    s = 2 ** (size - 1)
    # 1사분면에 위치한다면
    if 0 <= i < s and 0 <= j < s:
        return z(i, j, size - 1)
    # 2사분면에 위치한다면
    if 0 <= i < s and s <= j < 2 ** size:
        return s * s + z(i, j - s, size - 1)
    # 3사분면에 위치한다면
    if s <= i < 2 ** size and 0 <= j < s:
        return (s * s) * 2 + z(i - s, j, size - 1)
    # 4사분면에 위치한다면
    return (s * s) * 3 + z(i - s, j - s, size - 1)
    
print(z(r, c, n))