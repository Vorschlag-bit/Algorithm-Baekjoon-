from sys import stdin as input
n,m = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))

arr.sort()

# 중복조합
def prod(arr,m):
    s = set()
    def dfs(idx,cur):
        if len(cur) == m:
            s.add(tuple(cur))
            return
        
        for i in range(idx,len(arr)):
            cur.append(arr[i])
            dfs(i,cur)
            cur.pop()
    dfs(0,[])
    return s

p = prod(arr,m)
s = sorted(list(p))

for ele in s:
    print(' '.join(map(str,ele)))