n = int(input())

ans = 0

for i in range(5, n + 1, 5):
    num = i
    while num % 5 == 0:
        num /= 5
        ans += 1

print(ans)