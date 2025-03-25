import math
def solution(fees, records):
    minT,minF,perT,perF = fees[0], fees[1], fees[2], fees[3]
    cars = set()
    for rec in records:
        arr = rec.split()
        cars.add(arr[1])
    cars = sorted(cars)
    fee = dict()
    # 전체 주차시간
    total = dict()
    # 들어오는 시간
    In = dict()
    # 모든 차 총 주차시간 초기화
    for c in cars:
        total[c] = 0
    def minutes(time):
        t = time.split(":")
        return int(t[0]) * 60 + int(t[1])
    answer = []
    for rec in records:
        arr = rec.split()
        t,cn,command = arr[0],arr[1],arr[2]
        
        if command == "IN":
            In[cn] = minutes(t)
        else:
            intime = In[cn]
            parked = minutes(t) - intime
            total[cn] += parked
            In.pop(cn)
    # 들어오고 안 나간 놈들
    for cn,intime in In.items():
        total_time = (23*60+59) - intime
        total[cn] += total_time
    # 요금 청산
    for cn,totalT in total.items():
        # 기본 시간보다 같거나 작다면 기본요금
        if totalT <= minT:
            fee[cn] = minF
        else:
            totalT -= minT
            f = minF + math.ceil(totalT / perT) * perF
            fee[cn] = f
    for c in cars:
        answer.append(fee[c])
    print(answer)
    return answer