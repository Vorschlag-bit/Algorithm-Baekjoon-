import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

normal = {}
special = {}
service = set()
for i in range(a):
    name, price = input().split()
    price = int(price)
    normal[name] = price

for i in range(b):
    name, price = input().split()
    price = int(price)
    special[name] = price

for i in range(c):
    name = input().strip()
    service.add(name)

n = int(input())
# 총 주문 가격
nor = 0
spe = 0
spe_cnt = 0
ser = 0
check = True
for i in range(n):
    menu = input().strip()
    # 일반 메뉴인지 스페셜 메뉴인지 서비스 메뉴인지 검증
    if menu in normal:
        nor += normal[menu]
    elif menu in special:
        spe += special[menu]
        spe_cnt += 1
    else:
        ser += 1
if nor < 20000 and spe_cnt > 0:
    check = False
else:
    if nor + spe < 50000 and ser > 0:
        check = False
    if ser > 1:
        check = False

print("Okay" if check else "No")