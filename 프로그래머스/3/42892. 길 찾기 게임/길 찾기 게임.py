from sys import setrecursionlimit
setrecursionlimit(10000)
def solution(node):
    ans = [[],[]]
    node = [(i+1,x,y) for i,(x,y) in enumerate(node)]
    node.sort(key=lambda x: x[1])
    def recursion(n):
        if n:
            # idx,level,nodeNo
            root = (0,-1,0)
            for i,(node,x,y) in enumerate(n):
                if root[1] < y:
                    root = (i,y,node)
            l = n[:root[0]]
            r = n[root[0]+1:]
            ans[0].append(root[2])
            recursion(l)
            recursion(r)
            ans[1].append(root[2])
    # sudo root를 기준으로 좌,우
    recursion(node)
    return ans