import sys

n, m = map(int, sys.stdin.readline().strip().split())

arr = []
# 가격을 dictionary로 선언, key, value로 저장하기
p = {}
# 각 가격으로 달걀을 팔 때, 그 가격보다 높은 가격을 지불할 의향이 있는 모든 고객에게 판매 가능
# 정렬된 배열에서 i번째 가격으로 팔 때, (m-i)명의 고객이 구매가능
for i in range(m):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
# i = 0번째 가격(ex: 2)일 경우ㅡ 달걀 총 개수보다 더 팔 순 없으므로
# p에 저장되는 값 = (key)2: (value)2 * min(달걀 총 개수, 사람 수)
for i in range(m):
    p[arr[i]] = arr[i] * min(n, (m - i))

for k, v in p.items():
    if v == max(p.values()):
        print(k, v)
