import sys
from collections import deque

input = sys.stdin.readline
left = deque(input().strip()) # 커서 왼쪽에 담을 큐
right = deque() # 커서 오른쪽에 담을 큐
n = int(input()) # 명령어 수

for i in range(n):
    seq = input().strip()
    if seq == 'L':
        if left: # 왼쪽 q가 비어있지 않다면 오른쪽 q에 쌓기
            right.appendleft(left.pop())
    elif seq == 'D':
        if right: # 오른쪽 q가 비어있지 않다면 왼쪽 q에 쌓기
            left.append(right.popleft())
    elif seq == 'B':
        if left: # 왼쪽 q가 비어있지 않다면 왼쪽 q 마지막 요소 버리기
            left.pop()
    else: # 왼쪽 q에 쌓기
        _, alp = seq.split()
        left.append(alp)

print(''.join(left) + ''.join(right))