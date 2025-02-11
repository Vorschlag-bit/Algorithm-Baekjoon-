import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    dq = deque()
    cmd = input().rstrip()
    n = int(input().rstrip())
    put = input().rstrip()
    if n == 0:
        nums = []  # 빈 배열 처리
    else:
        nums = put.strip('[]').split(',')
        for num in nums:
            dq.append(num)
    
    # 명령어 처리
    error = False
    reverse = 1
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            reverse *= -1
        else:
            if not dq:
                error = True
                break
            if reverse < 0:
                dq.pop()
            else:
                dq.popleft()
    
    # 결과 출력
    if error:
        print("error")
    else:
        if reverse < 0:
            dq.reverse()
        ans = list(dq)
        print("[" + ",".join(ans) + "]")