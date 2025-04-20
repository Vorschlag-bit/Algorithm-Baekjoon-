def solution(arr):
    ans = [0,0]
    def recur(l,x,y):
        if l == 1:
            ans[arr[x][y]] += 1
            return
        else:
            c = arr[x][y]
            flag = True
            for i in range(x,x+l):
                for j in range(y,y+l):
                    if arr[i][j] != c:
                        flag = False
                        break
            if flag:
                ans[c] += 1
                return
            else:
                l //= 2
                recur(l,x,y)
                recur(l,x+l,y)
                recur(l,x,y+l)
                recur(l,x+l,y+l)
    recur(len(arr),0,0)
    return ans