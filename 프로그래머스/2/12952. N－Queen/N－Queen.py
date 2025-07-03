def solution(n):
    # 조합을 저장할 set
    visit = set()
    def check(i,j,col,d1,d2):
        # 행, 열, 대각선 집합에 n이 속하는지
        if j in col: return False
        if (i-j) in d1: return False
        if (i+j) in d2: return False
        return True
    
    # 행, 1-n**2 list, 금지열, 금지대각선 2가지
    def dfs(i,path,col,d1,d2):
        # 만약 idx == n and len(path) == n이면 visit에 추가
        if i == n and len(path) == n:
            key = frozenset(path)
            visit.add(key)
            return
        # idx행에서 j열에 q을 둘 수 있는지 판단
        for j in range(n):
            if check(i,j,col,d1,d2):
                col.add(j)
                d1.add((i-j))
                d2.add((i+j))
                dfs(i+1,path+[(i,j)],col,d1,d2)
                col.remove(j)
                d1.remove((i-j))
                d2.remove((i+j))
        # idx행에 둘 수 있는 곳이 없다면 return
        return
    dfs(0,[],set(),set(),set())
    return len(visit)