from sys import stdin as input

n = int(input.readline())
arr1 = list(map(int,input.readline().split()))
m = int(input.readline())
arr2 = list(map(int,input.readline().split()))

# a,b 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기
ans = []
a1 = 0
a2 = 0
while True:
    MAX = 0
    li = 0
    lj = 0
    for i in range(a1,n):
        for j in range(a2,m):
            if arr1[i] == arr2[j]:
                if MAX < arr1[i]:
                    MAX = arr1[i]
                    li = i
                    lj = j
    if MAX == 0: break
    ans.append(MAX)
    a1 = li + 1
    a2 = lj + 1

if not ans:
    print(0)
    exit()
print(len(ans))
print(' '.join(map(str,ans)))