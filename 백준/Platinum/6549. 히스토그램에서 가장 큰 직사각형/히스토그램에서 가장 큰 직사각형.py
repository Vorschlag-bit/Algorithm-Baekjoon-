import sys
from collections import deque

input = sys.stdin.readline
q = deque()
# (idx, height)
# 스택에는 반드시 오름차순으로 직사각형이 쌓이며, 최고 높이보다 낮은 막대를 만날 때
# 더이상 확장할 수 없으므로 그때 넓이를 계산한다.
def stack(arr):
    ans = 0
    # 마지막에 0을 집어넣어 반드시 스택이 비도록 함
    arr.append(0)
    for i in range(1, len(arr)):
        idx = i
        value = arr[i]
        # 자기보다 스택의 top이 높은 수일 경우 넓이 계산
        while q and q[-1][1] >= value:
            idx, h = q.pop()
            ans = max(ans, (i - idx) * h)
        # idx는 넓이가 계산된 경우, 시작점은 스택 속 자기보다 큰 수 중 가장 작은 점에서부터 시작
        q.append([idx, value])
    return ans
        


while True:
    arr = list(map(int, input().strip().split()))
    if arr[0] == 0:
        break
    print(stack(arr))