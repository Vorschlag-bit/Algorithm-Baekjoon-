from sys import stdin as input
n,m = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))
arr.sort()
# 순열
def perm(arr,m):
    s = set()
    visited = [False] * len(arr)
    def dfs(cur):
        if len(cur) == m:
            s.add(tuple(cur))
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                cur.append(arr[i])
                dfs(cur)
                cur.pop()
                visited[i] = False
    dfs([])
    return s

s = perm(arr,m)
l = sorted(list(s))
for t in l:
    print(' '.join(map(str,t)))