def solution(n, w, num):
    rows = (n + w - 1) // w
    ans = 0
    cnt = 1
    col = 0
    r = 0
    arr = [[0] * w for _ in range(rows)]
    for i in range(0,n,w):
        row = i // w
        if row % 2 == 0:
            for j in range(w):
                if cnt > n: break
                arr[row][j] = cnt
                if cnt == num:
                    col = j
                    r = row
                cnt += 1
        else:
            for j in range(w-1,-1,-1):
                if cnt > n: break
                arr[row][j] = cnt
                if cnt == num:
                    col = j
                    r = row
                cnt += 1
    for i in range(r,rows):
        if arr[i][col] == 0: break
        else: ans += 1
    return ans