import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
result = [0] * n
# (index, height) 리스트로 저장
stack = deque()
for i in range(n - 1, -1, -1):
    # 현재 빌딩보다 낮은 빌딩 다 제거
    while stack and stack[0][1] < arr[i]:
        stack.popleft()
    # 마지막은 항상 0
    if i == n - 1:
        result[n - 1] = 0
    # 스택이 비어있다면 가장 높은 빌딩이 된 것(= 이 인덱스 이후 모든 빌딩의 수)
    elif not stack:
        result[i] = n - 1 - i
    # 스택이 있다면 지금 빌딩보다 가장 가까우면서 제일 높은 빌딩의 인덱스 - 현재 빌딩 인덱스 - 1 = 개수
    else:
        result[i] = stack[0][0] - i - 1
    stack.appendleft((i, arr[i]))
print(sum(result))
