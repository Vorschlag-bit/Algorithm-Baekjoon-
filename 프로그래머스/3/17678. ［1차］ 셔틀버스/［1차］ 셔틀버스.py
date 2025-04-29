def t2s(t):
    h = str(t//60).rjust(2,"0")
    m = str(t%60).rjust(2,"0")
    return h+":"+m
def s2t(s):
    s = s.split(":")
    return int(s[0])*60+int(s[1])
def solution(n, t, m, times):
    ans = ''
    stack = []
    for time in times:
        stack.append(s2t(time))
    stack.sort(reverse=True)
    # 9시부터 n회 t분 간격, m명의 승객 탑승 가능
    # 도착 시각 중 제일 '늦은' 시각
    # 대기열 중 제일 뒤에 선다
    # 마지막 시간의 마지막 사람 -1분 or 비어있다면 그 시간
    # 09:00부터 t분
    for time in range(540,540+n*t,t):
        ride = []
        for p in range(m):
            if stack and stack[-1] <= time:
                ride.append(stack[-1])
                stack.pop()
        # 마지막 셔틀이라면
        if time == 540+(n-1)*t:
            # 모든 이가 셔틀을 탔다면
            if len(ride) == m:
                # 가장 마지막 사람 시간보다 -1분
                ans = t2s(ride[-1]-1)
            # 셔틀 자리가 있다면 마지막 시간
            else:
                ans = t2s(540+(n-1)*t)
    return ans