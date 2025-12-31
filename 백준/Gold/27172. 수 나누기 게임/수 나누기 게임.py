from sys import stdin as input
from collections import defaultdict

n = int(input.readline())
arr = list(map(int,input.readline().split()))
s = set(arr)
ans = defaultdict(int)
# 최댓값 100만
m = max(arr)

# a로 b를 나눌 때(b%a), 나머지가 0이면 a가 1점 획득, b%a의 나머지가 0이면 b가 1점 획득 그게 아니면 둘 다 0점
# 작은 걸로 큰 걸 나누면 최대공약수가 있어도, 소수만 분리됌.
# 반대로 큰 걸 작은 걸로 나눠도 b에게 소수가 있다면 나눠지지 않음
for ele in arr:
    # ele의 배수
    for num in range(ele * 2,m+1,ele):
        # ele의 배수가 집합에 있다면, ele += 1, num -= 1
        if num in s:
            ans[ele] += 1
            ans[num] -= 1

a = []
for ele in arr:
    a.append(ans[ele])
print(' '.join(map(str,a)))