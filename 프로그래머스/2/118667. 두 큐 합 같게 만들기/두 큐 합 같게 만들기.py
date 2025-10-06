from collections import deque
def solution(qu1, qu2):
    # 두 큐의 합을 같게 만드는 최소 횟수
    q1 = deque(qu1)
    q2 = deque(qu2)
    s1 = sum(q1)
    s2 = sum(q2)
    n = 0
    l = (len(q1) + len(q2))*2 + 2
    # 두 q를 모두 다 비웠음에도 두 큐의 합이 같아지지 않는다면 fail
    while n <= l:
        if s1 == s2: break
        # 큰 곳에서 작은 곳으로
        if s1 > s2:
            num = q1.popleft()
            s1 -= num
            s2 += num
            q2.append(num)
        elif s1 < s2:
            num = q2.popleft()
            s1 += num
            s2 -= num
            q1.append(num)
        n += 1
    ans = -1 if n > l else n
    return ans