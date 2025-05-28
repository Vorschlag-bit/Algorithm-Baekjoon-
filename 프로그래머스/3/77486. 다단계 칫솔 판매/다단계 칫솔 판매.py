def solution(en, ref, sel, amt):
    ans = []
    # 각 sel에 대해서, dfs
    graph = dict()
    total = dict()
    total['-'] = 0
    for e,r in zip(en,ref):
        graph[e] = r
        total[e] = 0
    def dfs(person, price):
        if person == '-':
            return
        if price // 10 < 1:
            total[person] += price
            return
        else:
            parent = graph[person]
            # 90
            total[person] += price - (price//10)
            # 10
            dfs(parent,price//10)
        
        
    for s,c in zip(sel,amt):
        dfs(s,c*100)
    for e in en:
        ans.append(total[e])
    return ans