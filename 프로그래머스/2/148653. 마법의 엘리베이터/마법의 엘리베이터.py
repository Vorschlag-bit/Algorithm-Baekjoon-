def solution(flr):
    ans = []
    def dfs(f,cnt):
        if f == 0:
            ans.append(cnt)
            return
        
        i = f % 10
        # up, down
        up,down = 10 - i, i
        if up > down:
            # 2554 -> 10 - 4 = 6(up), 4(down)
            dfs(f//10,cnt+down)
        elif up < down:
            # 4(up), 6(down)
            dfs(f//10+1,cnt+up)
        else:
            dfs(f//10,cnt+down)
            dfs(f//10+1,cnt+up)
    dfs(flr,0)
    return min(ans)