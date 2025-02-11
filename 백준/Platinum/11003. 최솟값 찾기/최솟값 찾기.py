import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dq = deque()
result = []

for i in range(n):
    # 1. 윈도우를 벗어난 값들을 제거
    while dq and dq[0][0] <= i - l:
        dq.popleft()
    
    # 2. 현재 값보다 큰 값들을 제거
    while dq and dq[-1][1] > arr[i]:
        dq.pop()
    
    # 3. 현재 값 추가
    dq.append((i, arr[i]))
    
    # 4. 항상 최솟값은 dq[0]에 있음
    print(dq[0][1], end=" ")
