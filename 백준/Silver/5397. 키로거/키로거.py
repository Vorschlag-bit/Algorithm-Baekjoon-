import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
left = deque()
right = deque()

for _ in range(n):
    typing = input().strip()
    left.clear()
    right.clear()
    for i in typing:
        if i == '<':
            if left: # 왼쪽 Q가 채워 있다면 오른쪽 Q로 옮기기
                right.appendleft(left.pop())
        elif i == '>':
            if right: # 오른쪽 Q가 채워 있다면 왼쪽 Q로 옮기기
                left.append(right.popleft())
        elif i == '-':
            if left: # 왼쪽 Q가 채워 있다면 가장 끝 제거
                left.pop()
        else: # 문자입력 (왼쪽 Q)
            left.append(i)
    print(''.join(left) + ''.join(right))