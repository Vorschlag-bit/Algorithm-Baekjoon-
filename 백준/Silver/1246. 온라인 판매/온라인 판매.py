import sys

n, m = map(int, sys.stdin.readline().strip().split())

arr = []
# 최소의 가격은 Pi 중 최솟값부터 시작해서 완전탐색 혹은 이분탐색으로 찾아보기
# 어느 한 가격(P)이 정해지면(이분이던 완탐이던) 모든 Pi를 순회하면서
# Pi가 P보다 크거나 같은 경우, 총 달걀 개수에서 -1, Pi가격 판매달걀 개수 + 1
# 배열을 완전히 다 순회한 후에는 정답과 비교, Pi판매개수 * Pi가 total보다 크다면 Pi와 cnt를 교체
for i in range(m):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

a = 0
b = 0
for i in arr:
    eggs = n
    total = 0
    cnt = 0
    for price in arr:
        if eggs > 0:
            if price >= i:
                cnt += 1
                eggs -= 1
    total = i * cnt
    if b < total:
        a = i
        b = total
print(f"{a} {b}")

