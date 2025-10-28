from collections import deque
def solution(players, m, k):
    ans = 0
    # 하루동안 최소 몇 번 증설해야하는지
    # players[i] = i~i시 사이의 이용자 수
    # m명 = 1대 서버 감당 가능
    # 한 번 증설한 서버는 k 시간 동안 운영
    # stack으로 stack[0]에 가장 빨리 증설한 서버 종료 시각 저장
    # 매번 시각과 종료 시각을 비교하기
    stack = deque()
    for i,p in enumerate(players):
        # 플레이하는 사람 없으면 pass
        if p == 0: continue
        st = i
        et = i+1
        while stack and stack[0] < et:
            stack.popleft()
        server = len(stack)
        # 현재 감당 가능 인원보다 더 많은 이가 플레이할 경우
        if server * m < p:
            total = p // m
            total -= server
            for _ in range(total):
                stack.append(st+k)
            ans += total
    return ans