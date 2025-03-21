from collections import Counter
def solution(friends, gifts):
    # dict에 이름을 key, 선물을 준 사람들의 배열을 value로 저장
    # gift에는 "준 사람, 받은 사람" 형태 리스트
    # {muzi: [frodo, frodo], frodo: [muzi,ryan]}
    # 선물지수 dict = {"muzi": 선물지수}
    # 2번 반복문을 돌면서 한 사람들이 자신을 제외한 다른 이들에게서 받아야할
    # 선물 계산, 1. 선물 주고 받은 양 계산 2. 0이거나 같으면 선물 지수 계산
    ans = 0
    present = dict()
    giftRate = dict()
    for person in friends:
        present[person] = []
        giftRate[person] = 0
    # 준 사람: [받은 사람, 받은 사람]
    for gift in gifts:
        giver, given = gift.split()
        present[giver].append(given)
    for giver in friends:
        for given in friends:
            # 자신은 패스
            if giver == given: continue
            # given이 선물을 받은 적있다면 그 수만큼 지수 상승
            if given in present[giver]:
                counter = Counter(present[giver])
                giftRate[giver] += counter[given]
            # giver가 선물을 받은 적이 있다면 그 수만큼 지수 감소
            if giver in present[given]:
                counter = Counter(present[given])
                giftRate[giver] -= counter[giver]
    # 다시 반복문을 돌면서, 한 사람이 다른 사람으로부터 선물을 받을지 말지 결정
    for person1 in friends:
        cnt = 0
        for person2 in friends:
            if person1 == person2: continue
            # 서로에게 준 선물을 비교 후, 같으면 선물지수 비교
            # P1given = {"muzi":2,"frodo":1}
            P1gift = Counter(present[person1]).get(person2, 0)
            P2gift = Counter(present[person2]).get(person1, 0)
            # P1이 많이 받았다면 cnt++
            if P1gift > P2gift:
                cnt += 1
            # P2가 많이 받았다면 넘어감
            elif P1gift < P2gift:
                pass
            # 같거나 주고 받은 적이 없다면 선물지수 비교
            else:
                # 선물지수가 더 높다면 선물 받을 예정
                if giftRate[person1] > giftRate[person2]:
                    cnt += 1
                # 아니면 넘어감
                else: pass
            ans = max(ans, cnt)
                    
    return ans