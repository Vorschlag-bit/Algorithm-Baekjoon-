# 1승을 계산할 수 있다.
# k승을 계산할 수 있다면 2k승, 2k + 1승도 o(1)으로 계산을 할 수 있다.
# a^b mod c

a, b, c = map(int, input().split())

def mod(a, b, c):
    if b == 1:
        return a % c
    
    n = mod(a, b//2, c)

    if b % 2 == 0:
        return (n * n) % c
    else:
        return (n * n * a) % c
print(mod(a, b, c))