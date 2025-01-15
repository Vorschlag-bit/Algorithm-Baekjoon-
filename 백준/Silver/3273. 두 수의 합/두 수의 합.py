import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().split()))
# 정렬
arr = sorted(arr)

t = int(input().strip())
ans = 0
l = 0
r = n - 1
while l < r:
    sum = arr[l] + arr[r]
    if sum == t:
        l += 1
        r -= 1
        ans += 1
    elif sum > t:
        r -= 1
    else:
        l += 1
print(ans)


