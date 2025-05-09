import heapq

def s2t(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m

def solution(book_time):
    # 1. 시각 정수화 + 정렬
    time = [(s2t(st), s2t(et)) for st, et in book_time]
    time.sort(key=lambda x: (x[0], x[1]))  # 입실 빠른 순

    q = []  # 종료시간 + 청소시간 min-heap (우선순위 큐)

    for st, et in time:
        # 2. 가장 빨리 끝나는 방을 하나만 꺼내서 확인
        if q and q[0] <= st:
            heapq.heappop(q)  # 방 재사용 가능

        # 3. 새 종료시간 + 청소시간 push
        heapq.heappush(q, et + 10)

    # 4. heap 크기 = 필요한 방의 수
    return len(q)