import sys;
k, n = map(int, sys.stdin.readline().strip().split())

arr = []


for i in range(k):
    arr.append(int(sys.stdin.readline()))

arr.sort()

min = 1
max = arr[-1]
ans = 0

while (min <= max):
    cnt = 0
    mid = (min + max) // 2

    for i in range(k):
        cnt += arr[i] // mid
    
    if cnt < n:
        max = mid - 1
    else:
        ans = mid
        min = mid + 1

print(ans)