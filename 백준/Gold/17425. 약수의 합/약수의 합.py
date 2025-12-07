# x보다 작거나 같은 모든 자연수 y의 f(y) (= y의 모든 약수를 더한 값)를 g(x)라고 부른다.
# g(n)을 구해보자
from sys import stdin as input
t = int(input.readline())

arr = []
m = 0
for _ in range(t):
    n = int(input.readline())
    m = max(m,n)
    arr.append(n)

f = [1] * (m+1)
for num in range(2,m+1):
    # num이 약수가 되는 수의 g[x]에 num 더하기
    for nxt in range(num, m+1, num):
        f[nxt] += num

# f에 대한 누적합(g)
for i in range(1,m):
    f[i+1] += f[i]

result = []
# 각 케이스별로 정답 출력
for n in arr:
    a = f[n]
    result.append(f[n])

print('\n'.join(map(str, result)))