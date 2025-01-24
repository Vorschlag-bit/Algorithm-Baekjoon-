import sys
input = sys.stdin.readline
n = int(input().strip())

arr = list(map(int, input().split()))
result = [0] * n
stack = [] # 인덱스, 높이 저장
# 차근차근 높은 타워 쌓기
for i in range(n):
    
    while stack and stack[-1][1] < arr[i]: # 낮은 높이부터 자기보다 높은 높이까지 탐색
        stack.pop() # 낮은 게 있다면 버리기
    
    if stack: # 자기보다 높은 가장 가까운 타워가 있다면 그 위치가 정답
        result[i] = stack[-1][0] + 1
    
    stack.append((i, arr[i]))

print(' '.join(map(str, result)))