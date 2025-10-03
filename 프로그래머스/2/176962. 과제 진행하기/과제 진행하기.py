def s2t(string):
    s = string.split(':')
    return int(s[0])*60+int(s[1])

def solution(plans):
    ans = []
    plan = []
    for name,start,pt in plans:
        plan.append((name,s2t(start),int(pt)))
    # 시간순으로 정렬
    plan.sort(key=lambda x: x[1])
    # name,start,dur
    stack = []
    # 현재 시각
    now = 0
    # n-1까지 이후 과제 시간을 고려하면서
    for i in range(len(plan)):
        # 마지막 과제는 항상 수행할 수 있음
        if i == len(plan) - 1:
            ans.append(plan[i][0])
            continue
        # 현재 시작해야 할 과제
        name,st,pt = plan[i]
        # 마지막 시각 or 현재 과제 시작 시간 중 큰 거
        # 다음에 시작해야 할 과제
        nxt_start = plan[i+1][1]
        # 다음 시작 과제보다 pt가 짧다면 수행
        if st + pt <= nxt_start:
            # 남는 시간
            rest = nxt_start - (st+pt)
            ans.append(name)
            # 남은 과제를 다 수행하거나 rest가 0 초과인 경우만
            while stack and rest > 0:
                nam,dur = stack.pop()
                # 남은 시간이 남은 과제 시간보다 같거나 크다면 완료(ans 추가)
                if dur <= rest:
                    rest -= dur
                    ans.append(nam)
                # 남은 시간이 과제 시간보다 적다면 그만큼만 수행하고 다시 넣기
                else:
                    dur -= rest
                    stack.append((nam,dur))
                    rest = 0
        # 길다면 최대한 마치고 stack에 보관
        else:
            rest = st + pt - nxt_start
            stack.append((name,rest))
    # stack에 남은 거 차례대로 수행
    while stack:
        name,dur = stack.pop()
        ans.append(name)
    return ans