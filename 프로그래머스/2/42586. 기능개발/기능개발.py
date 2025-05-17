from collections import deque
import math
def solution(pr, speeds):
    ans = []
    # pr의 순서대로 배포가 되어야만 한다
    q = deque()
    # 프로세스가 완료되는 데 소요되는 시간을 append
    # (5), 10 -> q[0] < days
    for i,p in enumerate(pr):
        days = math.ceil((100-pr[i])/speeds[i])
        if q:
            if q[0] < days:
                ans.append(len(q))
                q = deque()
        q.append(days)
    ans.append(len(q))
    return ans