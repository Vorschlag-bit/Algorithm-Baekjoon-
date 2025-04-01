from collections import deque
import math
def solution(players, m, k):
    stack = deque()
    ans = 0
    # 매 시간마다 현재 서버 개수 계산(감당 가능한지)
    # 서버 종료 시간을 stack 속에 저장(오름차순), 매 시간마다 stack top과 시간 비교 후,
    # 현재 시각이 더 크면 감소
    servers = 0
    for idx,p in enumerate(players):
        # 서버 종료
        if stack:
            while stack and stack[0][0] <= idx:
                endTime,cnt = stack.popleft()
                servers -= cnt
        # 현재 감당 가능한 사람의 수
        able = servers * m + (m-1)
        if able < p:
            need = math.ceil((p - able) / m)
            ans += need
            servers += need
            # 종료 시간 누적(시간,개수)
            stack.append((idx+k,need))
    print(ans)
    return ans