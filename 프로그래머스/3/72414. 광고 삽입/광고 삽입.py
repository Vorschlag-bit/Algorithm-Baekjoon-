def s2t(s):
    h = int(s[0]) * 60 * 60
    m = int(s[1]) * 60
    sec = int(s[2])
    return h + m + sec

def t2s(t):
    print(t)
    h = t // 3600
    hour = str(h).rjust(2,'0')
    t -= h * 3600
    m = t // 60
    minu = str(m).rjust(2,'0')
    s = t - (m*60)
    sec = str(s).rjust(2,'0')
    return hour+':'+minu+':'+sec

def solution(play_time, adv_time, logs):
    ans = ''
    # 누적합
    play = []
    total = s2t(play_time.split(':'))
    at = s2t(adv_time.split(':'))
    if total == at: return '00:00:00'
    for pt in logs:
        pt = pt.split('-')
        st = pt[0].split(':')
        et = pt[1].split(':')
        start = s2t(st)
        end = s2t(et)
        play.append((start,end))
    play.sort(key=lambda x: x[0])
    view = [0] * (total+1)
    # 시청 누적
    for st,et in play:
        view[st] += 1
        view[et] -= 1
    # 누적합 반영
    for i in range(total):
        view[i+1] += view[i]
    prefix = [0] * (total+1)
    for i in range(total):
        prefix[i+1] = prefix[i] + view[i]
    max_stack = 0
    time = 0
    for st in range(total-at+1):
        et = st + at
        # 누적 시간 계산
        stack = prefix[et] - prefix[st]
        if stack > max_stack:
            max_stack = stack
            time = st
    return t2s(time)