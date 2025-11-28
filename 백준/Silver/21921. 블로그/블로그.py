from sys import stdin as input

n,x = map(int,input.readline().split())

# x일 동안 가장 많이 들어온 방문자 수 출력.
# 최대 방문자 수가 0이 아닌 경우 해당 날짜가 몇 개인지 개수 출력
arr = list(map(int,input.readline().split()))

ans = 0
l = 0
s = 0
cnt = 1
for r in range(len(arr)):
    s += arr[r]
    # 3 - 1
    if r-l+1 == x:
        if ans < s:
            ans = s
            cnt = 1
        elif ans == s:
            cnt += 1
        s -= arr[l]
        l += 1

if ans == 0:
    print("SAD")
    exit()
else:
    print(ans)
    print(cnt)