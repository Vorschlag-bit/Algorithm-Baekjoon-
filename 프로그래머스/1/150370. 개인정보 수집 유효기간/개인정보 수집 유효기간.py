def solution(today, ts, ps):
    # 보관 가능한 것은 + 개월 - 1일까지!
    ans = []
    # 어차피 모든 달은 28일 기준이므로, 파싱해서 처리하는 게 맞는 듯?
    arr = list(today.split('.'))
    # 오늘의 년,월,일
    today = int(arr[0])*12*28 + int(arr[1])*28 + int(arr[2])
    terms = {v[0]: v[2:] for v in ts}
    def getDay(day, month):
        y,m,d = map(int,day.split('.'))
        m += int(month)
        return y * 12 * 28 + m * 28 + d - 1
    # 개인정보 수집일자 + 약관 유효기간 < 오늘 => 파기 대상
    for idx,info in enumerate(ps):
        d, term = info.split()
        # day에 약관 유효기간 더하기(달 - 하루)
        expired = getDay(d, terms[term])
        if today > expired:
            ans.append(idx+1)
    print(ans)
    return ans