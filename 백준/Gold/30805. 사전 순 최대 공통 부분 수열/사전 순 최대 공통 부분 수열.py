from sys import stdin as input

n = int(input.readline())
arr1 = list(map(int,input.readline().split()))
m = int(input.readline())
arr2 = list(map(int,input.readline().split()))

# a,b 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기

# 최대한 앞에 큰 숫자가 오면 된다.
# 두 배열 공통 최대 수
MAX = 0
for i in range(n):
    for j in range(m):
        if arr1[i] == arr2[j]:
            MAX = max(MAX, arr1[i])

# 공통 부분 없으면 끝
if MAX == 0:
    print(0)
    exit()

a1_s = arr1.index(MAX) + 1
a2_s = arr2.index(MAX) + 1

ans = [MAX]

# while문으로 단계적 점프
while True:
    common = 0
    # 남은 2배열의 공통최댓값 찾기
    for i in range(a1_s,n):
        for j in range(a2_s,m):
            if arr1[i] == arr2[j]:
                common = max(common, arr1[i])
    if common == 0: break
    ans.append(common)
    a1_s = arr1.index(common, a1_s) + 1
    a2_s = arr2.index(common, a2_s) + 1

print(len(ans))
print(' '.join(map(str,ans)))