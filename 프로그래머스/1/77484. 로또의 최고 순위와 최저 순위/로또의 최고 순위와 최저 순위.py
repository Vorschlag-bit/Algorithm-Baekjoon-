def solution(lottos, win_nums):
    l = [6,6,5,4,3,2,1]
    c_0 = lottos.count(0)
    cnt = 0
    for n in lottos:
        if n in win_nums: cnt+=1
    return l[c_0+cnt], l[cnt]