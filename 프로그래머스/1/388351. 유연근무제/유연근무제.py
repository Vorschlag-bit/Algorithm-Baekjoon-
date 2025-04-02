def solution(schedules, times, start):
    ans = 0
    for idx,sch in enumerate(schedules):
        access_time = (sch // 100) * 60 + sch % 100 + 10
        present = True
        for j in range(7):
            day = (start + j) % 7
            if day == 0 or day == 6:
                continue
            inT = (times[idx][j] // 100) * 60 + times[idx][j] % 100
            if access_time < inT:
                present = False
                break
        if present:
            ans += 1
    return ans