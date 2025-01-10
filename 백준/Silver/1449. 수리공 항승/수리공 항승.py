import sys
input = sys.stdin.readline

n, l = map(int, input().split())

check = [False] * 1001

nums = list(map(int, input().split()))
nums = sorted(nums)
ans = 0
for i in nums:
    if not check[i]:
        for j in range(i, min(i + l, 1001)):
            check[j] = True
        ans += 1
print(ans)


