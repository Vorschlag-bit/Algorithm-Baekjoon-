from collections import deque
def solution(c1, c2, goal):
    flag = True
    q1 = deque(c1)
    q2 = deque(c2)
    g = deque(goal)
    while g:
        t = g.popleft()
        if q1:
            e1 = q1.popleft()
        if q2:
            e2 = q2.popleft()
        if t == e1: q2.appendleft(e2)
        elif t == e2: q1.appendleft(e1)
        else:
            flag = False
            break
    return "Yes" if flag else "No"