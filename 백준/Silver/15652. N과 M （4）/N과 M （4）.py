from sys import stdin as input
n,m = map(int,input.readline().split())

# 중복순열
def perm(arr,r):
    result = []
    def dfs(path,r):
        nonlocal result,arr
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if len(path) > 0 and path[-1] <= arr[i]:
                path.append(arr[i])
                dfs(path,r)
                path.pop()
            elif len(path) == 0:
                path.append(arr[i])
                dfs(path,r)
                path.pop()
    dfs([],r)
    return result

arr = [i+1 for i in range(n)]
for p in perm(arr,m):
    print(' '.join(map(str,p)))