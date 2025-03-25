n = int(input())
Ai = list(map(int, input().split()))
b,c = map(int, input().split())
ans = 0
for idx in range(len(Ai)):
    Ai[idx] -= b
    ans += 1
    if Ai[idx] > 0:
        if Ai[idx] <= c:
            ans += 1
        else:
            q,r = divmod(Ai[idx],c)
            if r == 0:
                ans += q
            else:
                ans += 1 + q
print(ans)