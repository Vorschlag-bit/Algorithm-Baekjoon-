from collections import defaultdict
import heapq
def split(n,k):
    result = []
    def dfs(path, rest_s, rest_k):
        # path = 지금까지 고른 배열
        # rest_s = 남은 합
        # rest_k = 남은 k
        if rest_k == 0:
            if rest_s == 0:
                result.append(path[:])
            return
        min_v = 1
        max_v = rest_s - (rest_k-1)
        if max_v < min_v: return
        for value in range(min_v, max_v+1):
            path.append(value)
            dfs(path, rest_s - value, rest_k-1)
            path.pop()
    dfs([],n,k)
    return result
def solution(k, n, reqs):
    ans = float('inf')
    # 기다린 시간의 합이 최소
    # n명의 멘토를 k로 최소 몫 1이상 나누기
    # (시작, 끝)으로 넣고
    # if len(stack) == s[c] and stack[-1]: 기다리는 시간 계산해서 더해주기
    for s in split(n,k):
        w = 0
        s = [0] + s
        counsling = defaultdict(list)
        for i in range(1,k+1):
            # 각 상담 유형마다 개수에 맞는 상담사 heap을 생성(끝나는 시간 기준)
            for _ in range(s[i]):
                heapq.heappush(counsling[i],0)
        for a,b,c in reqs:
            end = heapq.heappop(counsling[c])
            if end > a:
                w += end - a
                a = end
            heapq.heappush(counsling[c],a+b)
        ans = min(ans,w)
    return ans