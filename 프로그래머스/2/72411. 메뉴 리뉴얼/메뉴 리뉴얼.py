from itertools import combinations as comb
def solution(orders, course):
    ans = []
    # 최소 2가지 이상의 단품 메뉴, 최소 2명 이상의 손님으로부터 주문된 단품 메뉴
    # 메뉴 구성이 여러 개면 모두 배열에 담아 return
    o = []
    for order in orders:
        s = list(order)
        s.sort()
        o.append(''.join(s))
    for r in course:
        d = dict()
        for order in o:
            # 해당 문자로 r개 코스 못 만들면 pass
            if len(order) < r: continue
            # 문자열 문자 배열로 만들기
            chrs = list(order)
            # 문자 배열로 r개의 조합 생성
            for c in comb(chrs,r):
                d[c] = d.get(c,0) + 1
        # r개로 만든 게 없으면 pass
        if not d.keys(): continue
        # 가장 많이 주문 받은 메뉴     
        most = max(d,key=lambda x: d[x])
        num = d[most]
        # 2개 이상이여야 함
        if num < 2: continue
        for k,v in d.items():
            if num == v:
                ans.append(''.join(k))
    ans.sort()
    return ans