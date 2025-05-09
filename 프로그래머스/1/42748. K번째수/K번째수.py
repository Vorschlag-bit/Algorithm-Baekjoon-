def solution(arr, cmds):
    ans = []
    for i,j,k in cmds:
        # 1 - 4
        a = arr[i-1:j]
        a.sort()
        ans.append(a[k-1])
    return ans