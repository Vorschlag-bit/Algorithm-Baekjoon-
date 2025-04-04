def solution(band, h, a):
    # band[0] = 시전 시간, band[1] = 초당 회복량, band[2] = 추가 회복량
    heal_time,perH,perfectH = band[0],band[1],band[2]
    combo = 1
    ai = 0
    lasttime = a[-1][0]
    cur_h = h
    def check(health):
        if health <= 0: return False
        else: return True
    
    for t in range(1,lasttime+1):
        print("현재 체력: " + str(cur_h))
        print("연속 감기: " + str(combo))
      # 현재 시간에 공격이 있는지 확인
        if t == a[ai][0]:
            cur_h -= a[ai][1]
            ai += 1
            combo = 1
      # 없다면 comb * 
        else:
            print("붕대감기(초):" + str(t))
            cur_h += perH
            if combo == heal_time:
                cur_h += perfectH
                combo = 1
            else:
                combo += 1
        if check(cur_h):
            # h 안 넘게 맞추기
            if cur_h > h:
                cur_h = h
        else: return -1
        print("한 턴 끝나고 체력: " + str(cur_h))
    return cur_h