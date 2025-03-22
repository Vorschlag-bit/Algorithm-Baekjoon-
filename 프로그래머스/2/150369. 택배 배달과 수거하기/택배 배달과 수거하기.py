def solution(cap, n, ds, ps):
    ans = 0
    deli = [[(i+1),ds[i]] for i in range(len(ds)) if ds[i] > 0]
    pick = [[(i+1),ps[i]] for i in range(len(ps)) if ps[i] > 0]
    
    def makeD(stack):
        dis = 0
        amount = 0
        while stack:
            # 수거 or 배달해야 할 집(idx,개수)
            target = stack.pop()
            # 최대 배달 거리
            if target[0] > dis:
                dis = target[0]
            # 개수가 용량보다 크다면 다시 넣기
            if amount + target[1] > cap:
                target[1] = (amount + target[1] - cap)
                stack.append(target)
                return dis
            # 아니면 배달(수거)
            amount += target[1]
        return dis
    while deli or pick:
        ans += max(makeD(deli), makeD(pick))*2
    return ans