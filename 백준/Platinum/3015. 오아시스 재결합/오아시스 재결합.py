import sys
from collections import deque
q = deque()
# (키 , 연속으로 나온 사람의 수)
input = sys.stdin.readline
n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
result = 0
for i in arr:
    # 자기보다 큰 사람이 나올 때까지 popleft
    while q and q[0][0] < i:
        result += q.popleft()[1]
    # 비어있다면 그 사람은 왼쪽에 있는 모든 사람을 다 볼 수 있다.
    if not q:
        q.appendleft((i, 1))
        continue
    # 연속으로 이어진 사람이 있다면 +1
    if q[0][0] == i:
        cnt = q.popleft()[1]
        result += cnt
        # 더 큰 사람이 있다면 한 명 더 볼 수 있음
        if q:
            result += 1
        q.appendleft((i, cnt + 1))
    else:
        result += 1
        q.appendleft((i, 1))
print(result)