def solution(arr):
    ans = []
    ans.append(arr[0])
    for e in arr:
        if e != ans[-1]: ans.append(e)
    return ans