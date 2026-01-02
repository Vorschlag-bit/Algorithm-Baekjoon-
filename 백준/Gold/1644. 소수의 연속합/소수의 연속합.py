from sys import stdin as input

n = int(input.readline())
# n까지 소수를 담을 배열
arr = []

check = [True] * (n+1)
check[0],check[1] = False,False
#
for i in range(2,int(n**0.5)+1):
    if check[i]:
        for j in range(i+i,n+1,i):
            check[j] = False

for num in range(1,n+1):
    if check[num]: arr.append(num)

# 투 포인터
l = 0
cur = 0
ans = 0
for r in range(len(arr)):
    cur += arr[r]
    while cur >= n:
        if cur == n: ans += 1
        cur -= arr[l]
        l += 1
print(ans)