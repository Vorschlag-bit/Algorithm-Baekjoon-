def s2t(s):
    sp = s.split(":")
    return int(sp[0]) * 60 + int(sp[1])

def solution(fees, records):
    ans = []
    # 누적 주차 시간을 구해야 함
    total = dict()
    # 입차 관리(k - 차량 번호, v - 입차 시간)
    In = dict()
    # 출차 관리
    Out = dict()
    for record in records:
        rec = record.split(" ")
        time = s2t(rec[0])
        num = rec[1]
        # In or Out
        r = rec[2]
        # in
        if r == 'IN':
            In[num] = time
        # out
        else:
            Out[num] = time
            in_t = In[num]
            total[num] = total.get(num,0) + (time-in_t)
            In[num] = -1
    
    max_t = s2t("23:59")
    # 입차 기반으로 번호 카운팅
    for num,in_t in In.items():
        if in_t != -1:
            # 출차 시간은 없을 경우 "23:59"
            total[num] = total.get(num,0) + (max_t-in_t)
    # 차량 번호로 정렬하기 위해 임시 저장(번호,요금)
    temp = []
    for num,t in total.items():
        price = fees[1]
        if t > fees[0]:
            over = t - fees[0]
            # 단위 시간으로 나눠 떨어질 경우 그대로
            if over % fees[2] == 0:
                r = over // fees[2]
                price += r * fees[3]
            # 안 나눠떨어지면 + 1
            else:
                r = (over // fees[2]) + 1
                price += r * fees[3]
        temp.append((int(num),price))
    temp.sort(key=lambda x: x[0])
    for num,p in temp:
        ans.append(p)
    # 어떤 차량이 입차된 후에 출차된 내역이 없다면 23:59에 출차된 것으로 간주
    # 1. '누적' 주차 시간이 기본 시간 이하일 경우 기본 요금 청구
    # 2. '누적' 주차 시간이 기본 시간 초과일 경우 기본 요금 + 초과된 시간에 대해 단위 시간별 단위 요금 청구
    # 초과 시간이 단위 시간으로 나눠 떨어지지 않으면 올림
    # 차량 번호가 작은 자동차부터 주차 요금을 차례대로 배열에 담아 return
    return ans