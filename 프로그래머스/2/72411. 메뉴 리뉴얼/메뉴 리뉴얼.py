from itertools import combinations as comb
from collections import defaultdict
def solution(orders, course):
    answer = []
    c_set = defaultdict(set)
    # 메뉴 개수에 따른 최대 주문 수를 저장할 dict
    dic = {c:0 for c in course}
    for order in orders:
        for r in course:
            if r > len(order): continue
            for combo_menu in comb([char for char in order],r):
                # ABCFG -> (A,B), (A,C), (A,F), (A,G) ...
                # 이미 있는 조합 메뉴라면 패스
                combo_menu = tuple(sorted(combo_menu))
                cnt = 0
                for o in orders:
                    if set(combo_menu).issubset(set(tuple(o))):
                        cnt += 1
                if cnt >= 2:
                    if dic[r] < cnt:
                        dic[r] = cnt
                        c_set[r] = {combo_menu}
                    elif dic[r] == cnt:
                        c_set[r].add(combo_menu)
    for r in course:
        answer += [''.join(menu) for menu in c_set[r]]
    return sorted(answer)