from sys import stdin as input

t = int(input.readline())

n = int(input.readline())
A = list(map(int,input.readline().split()))

m = int(input.readline())
B = list(map(int,input.readline().split()))

# A의 부 배열의 합 + B의 부 배열의 합 = t가 되는 모든 부 배열의 쌍 개수
ans = 0
# A,B의 부 배열의 모든 경우의 수는 1000 * 999 // 2 => 대략 50만
# A + B = t -> A = t - B or B = t - A를 만족하는 특정값이 존재하는지 판단하는 문제
bSum = []

# k = A 부 배열의 합, v = 그 합의 개수
Ad = dict()

for i in range(n):
    s = 0
    for j in range(i,n):
        s += A[j]
        Ad[s] = Ad.get(s,0) + 1


for i in range(m):
    s = 0
    for j in range(i,m):
        s += B[j]
        bSum.append(s)

# bSum을 순회하면서 B - t가 Ad에 몇 개 있는지 카운트
for num in bSum:
    tx = t - num
    ans += Ad.get(tx,0)

print(ans)