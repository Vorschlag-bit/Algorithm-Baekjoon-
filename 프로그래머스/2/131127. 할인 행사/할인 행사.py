def solution(want, num, dis):
    ans = 0
    # 10의 길이동안 품목과 개수가 완전히 일치하는 시작일이 몇 개인가
    # 14 - 5 = 9, 0 - 9
    for i in range(0,len(dis)-9):
        dic = dict()
        for j in range(i,i+10):
            dic[dis[j]] = dic.get(dis[j],0) + 1
        flag = True
        for w,cnt in zip(want,num):
            if dic.get(w,0) != cnt:
                flag = False
                break
        if flag:
            ans += 1
    return ans