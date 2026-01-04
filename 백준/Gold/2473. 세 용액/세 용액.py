from sys import stdin as input

# 세 가지 용액의 합이 0에 가장 가까운 수를 출력
n = int(input.readline())
arr = list(map(int,input.readline().split()))

# 특정 수 m에 대한 최적의 수는 -m
# 나머지 두 수의 합이 -m을 만족할 수 있는 최적의 수를 찾아야 함...
# 5000 * 5000 = 2천5백만

arr.sort()
# 정답은 1. -m에 최대한 가까워야 함. 2. -m + m이 0에 가까워야 함
ans = float('inf')
a,b,c = 0,0,0
for i,m in enumerate(arr):
    t = -m
    l = i+1
    r= n-1
    while r > l:
        s = arr[r] + arr[l]
        if ans > abs(arr[i] + arr[r] + arr[l]):
            ans = abs(arr[i] + arr[r] + arr[l])
            a,b,c = i,l,r
        # 목표한 것보다 크다면 r을 줄이기
        if s > t: r -= 1
        # 목표한 것보다 작다면 l을 늘리기
        else: l += 1
ans_l = sorted([arr[a],arr[b],arr[c]])
print(' '.join(map(str,ans_l)))