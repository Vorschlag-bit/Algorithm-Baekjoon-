from collections import defaultdict
def solution(tickets):
    l = len(tickets)
    ans = []
    t = defaultdict(list)
    for f,e in tickets:
        t[f].append(e)
    for k in t.keys():
        t[k].sort()
    visit = set()
    def dfs(cur,used,path):
        nonlocal l,ans
        if len(used) == l:
            ans.append(path[:])
            return
        
        for i,nxt in enumerate(t[cur]):
            key = (cur,nxt,i)
            if key in used: continue
            used.add(key)
            path.append(nxt)
            dfs(nxt,used,path)
            path.pop()
            used.remove(key)
    dfs("ICN",set(),["ICN"])
    return sorted(ans)[0]