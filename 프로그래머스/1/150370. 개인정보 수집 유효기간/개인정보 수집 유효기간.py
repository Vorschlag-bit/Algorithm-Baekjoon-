def solution(today, ts, ps):
    # 보관 가능한 것은 + 개월 - 1일까지!
    ans = []
    # 어차피 모든 달은 28일 기준이므로, 파싱해서 처리하는 게 맞는 듯?
    arr = list(today.split('.'))
    # 오늘의 년,월,일
    year, month, day = arr[0],arr[1],arr[2]
    td = int(year) * 10000 + int(month) * 100 + int(day)
    terms = dict()
    for t in ts:
        name, months = t.split()
        terms[name] = int(months)
    def getDay(day, month):
        y,m,d = map(int,day.split('.'))
        m += month
        # 12 + 3 = 15
        y += (m-1) // 12
        m  = ((m-1)%12) + 1
        d -= 1
        if d == 0:
            m -= 1
            if m == 0:
                y -= 1
                m =12
            d = 28
        return y * 10000 + m * 100 + d
    # 개인정보 수집일자 + 약관 유효기간 < 오늘 => 파기 대상
    for idx,info in enumerate(ps):
        d, term = info.split()
        # day에 약관 유효기간 더하기(달 - 하루)
        expired = getDay(d, terms[term])
        flag = False
        if td > expired:
            flag = True
        if flag:
            ans.append(idx+1)
    print(ans)
    return ans