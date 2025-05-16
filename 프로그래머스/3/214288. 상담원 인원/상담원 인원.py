from collections import defaultdict
import heapq
def split(n,k):
    result = []
    def dfs(path,idx):
        if idx == k:
            if sum(path) == n:
                result.append(path[:])
            return
        for i in range(1,n+1):
            if sum(path) + i + (k - idx - 1) <= n:
                dfs(path+[i], idx+1)
    dfs([],0)
    return result
def solution(k, n, reqs):
    ans = float('inf')
    # 멘토 수n를 상담 유형k만큼 나누기
    # 그렇게 나눈 걸 바탕으로 heap을 사용해서 기다린 시간 계산
    for com in split(n,k):
        com = [0] + com
        dic = defaultdict(list)
        wait = 0
        for i in range(1,k+1):
            for _ in range(com[i]):
                heapq.heappush(dic[i], 0)
        for a,b,c in reqs:
            # c번 유형 상담을 a분 ~ b분 동안 상담을 요청
            end = heapq.heappop(dic[c])
            if end > a:
                wait += end - a
                a = end
            heapq.heappush(dic[c],a+b)
        ans = min(ans, wait)
    return ans