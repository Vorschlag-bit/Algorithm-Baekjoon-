from sys import stdin as input

n = int(input.readline())
arr = list(map(int,input.readline().split()))
m = int(input.readline())
q = []
# 0-based
for _ in range(m):
    s,e = map(int,input.readline().split())
    q.append((s-1,e-1))
# dp로 모든 인덱스에 대한 펠린드롬 여부
# dp[i][j] = i-j까지의 문자열이 펠린드롬인지 판단
dp = [[False] * n for _ in range(n)]
# 1자리,연속된 2자리 = 모두 펠린드롬
# 1자리
for i in range(n):
    dp[i][i] = True
# 연속된 2자리 -> 0,1 1,2 2,3
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True
# 3자리부터 i = 0 ~ n-1까지 순회, j는 i+2부터 n-1까지
# i = 0, j = 2일 경우 dp[1][1] = True and arr[i] == arr[j]면 dp[i][j]도 True

for l in range(2,n):
    # 연속된 길이가 l+1인 것
    for i in range(n-l):
        if dp[i+1][i+l-1] == True and arr[i] == arr[i+l]: dp[i][i+l] = True

ans = []

for s,e in q:
    if dp[s][e] == True:
        ans.append(1)
    else: ans.append(0)

print('\n'.join(map(str,ans)))