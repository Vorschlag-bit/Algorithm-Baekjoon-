import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left = 0
ans = 0
dic = {}
for right in range(n):
    dic[arr[right]] = dic.get(arr[right], 0) + 1
    while len(dic) > 2:
        dic[arr[left]] -= 1
        if dic[arr[left]] == 0:
            del dic[arr[left]]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)