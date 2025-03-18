from collections import deque
def getPay(h,a,t):
    for c in h:
        if t - c in a:
            h.remove(c)
            a.remove(t-c)
            return True
    return False
def solution(c, cards):
    t = len(cards) + 1
    hand = cards[:len(cards)//3]
    rest = deque(cards[len(cards)//3:])
    cnt = 1
    arr = []
    while c >= 0 and rest:
        arr.append(rest.popleft())
        arr.append(rest.popleft())
        # 손에 있는 걸로만 내기
        if getPay(hand,hand,t):
            pass
        elif c >= 1 and getPay(hand,arr,t):
        # arr에 있는 2개 중 1개 사용했으면 
            c -= 1
        elif c >= 2 and getPay(arr,arr,t):
        # arr에 있는 2개 모두 사용
            c -= 2
        else:
            break
        cnt += 1
    return cnt