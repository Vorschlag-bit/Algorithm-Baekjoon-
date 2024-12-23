import sys;
from collections import deque;

n = int(sys.stdin.readline().strip())
dq = deque()
# indexError 방지 0 넣기
dq.append(0)
# split()으로 나누고 map으로 각 항목을 정수로 변환 후 리스트화
arr = list(map(int, sys.stdin.readline().split()))

idx = 1 # stack에 차례대로 들어가 저장될 수
stack = True # 스택이 차례대로 쌓이는지 판별

for i in range(n):
    # 1. 배열에서 차례로 꺼낸다.
    num = arr[i]
    # stack에서 top이 필요한 수인지 판별
    while dq[-1] == idx:
        dq.pop()
        idx += 1
    # num == idx면 패스
    if num == idx:
        idx += 1
    else:
        # 내림차순 보장
        if dq[-1] != 0 and dq[-1] < num:
            stack = False
            break
        dq.append(num)
print("Nice" if stack else "Sad")
