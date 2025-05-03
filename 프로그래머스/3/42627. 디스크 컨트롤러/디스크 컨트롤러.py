import heapq
def solution(jobs):
    ans = 0
    n = len(jobs)
    arr = []
    for i,j in enumerate(jobs):
        s,cost = j
        arr.append((cost,s,i))
    arr.sort(key=lambda x: -x[1])
    # 소요시간 짧, 요청시각 빠름, 작업 번호 작음 순으로 우선순위
    # jobs에서 작업 하나를 꺼냄. 해당 작업을 마무리
    # 마무리한 시간 기록보다 요청 시각이 작은 작업들을 jobs에서 제거 후, heaq에 넣기
    # heaq에서 작업 마무리
    q = []
    heapq.heappush(q,arr.pop())
    # 현재 시각
    time = 0
    while q:
        cost,s,idx = heapq.heappop(q)
        # 현재 시각 계산
        if s >= time:
            time = s + cost
        else:
            time += cost
        # 반환 시간 계산
        ans += time - s
        while arr and arr[-1][1] <= time:
            heapq.heappush(q,arr.pop())
        # 시간 간격이 너무 길어서 heapq가 빈다면 채우기
        if not q and arr:
            heapq.heappush(q,arr.pop())
            time = max(time, q[0][1])
    return ans // n