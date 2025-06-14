def solution(a, b):
    idx = 5
    d = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    m = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    month = 0
    day = 0
    while a != month:
        day += m[month]
        month += 1
    day += b-1
    day %= 7
    return d[(idx+day)%7]