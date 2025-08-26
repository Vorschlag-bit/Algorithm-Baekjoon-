from sys import stdin as input
n,m = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))
arr.sort()
# 조합
def perm(arr,r):
    result = []
    def dfs(path,used,r):
        nonlocal result
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if used[i]: continue
            used[i] = True
            path.append(arr[i])
            dfs(path,used,r)
            used[i] = False
            path.pop(-1)
    dfs([],[False]*len(arr),r)
    return result

for c in perm(arr,m):
    print(' '.join(map(str,c)))