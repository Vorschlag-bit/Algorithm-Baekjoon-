def check(u,b):
    if len(u) != len(b):
        return False
    for i,char in enumerate(b):
        if char != '*' and char != u[i]: return False
    return True

def dfs(idx,user,ban,path,visit,result):
    if idx == len(ban):
        result.add(frozenset(path))
        return
    for i,usr in enumerate(user):
        if not visit[i] and check(usr,ban[idx]):
            visit[i] = True
            path.append(usr)
            dfs(idx+1,user,ban,path,visit,result)
            visit[i] = False
            path.pop()

def solution(user, ban):
    visit = [False]*len(user)
    result = set()
    dfs(0,user,ban,[],visit,result)
    return len(result)