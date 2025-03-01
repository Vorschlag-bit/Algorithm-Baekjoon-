def solution(numbers, hand):
    ans = ''
    def dis(ai, aj, bi, bj):
        return abs(ai - bi) + abs(aj - bj)
    l = [1, 4, 7]
    r = [3, 6, 9]
    m = [2, 5, 8, 0]
    lh = (3, 0)
    rh = (3, 2)
    for n in numbers:
        # 왼손으로 눌러야만 하는 경우
        if n in l:
            ans += 'L'
            lh = (l.index(n), 0)
        # 오른손으로 눌러야만 하는 경우
        elif n in r:
            ans += 'R'
            rh = (r.index(n), 2)
        # 가운데에 있는 수라면
        else:
            ld = dis(lh[0], lh[1], m.index(n), 1)
            rd = dis(rh[0], rh[1], m.index(n), 1)
            if ld < rd:
                ans += 'L'
                lh = (m.index(n), 1)
            elif ld > rd:
                ans += 'R'
                rh = (m.index(n), 1)
            # 둘의 거리가 같다면
            else:
                if hand == 'left':
                    ans += 'L'
                    lh = (m.index(n), 1)
                else:
                    ans += 'R'
                    rh = (m.index(n), 1)
    return ans