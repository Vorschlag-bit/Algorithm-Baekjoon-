def s2t(s):
    s = s.split(":")
    return int(s[0])*60+int(s[1])
def solution(plans):
    ans = []
    for p in plans:
        p[1] = s2t(p[1])
        p[2] = int(p[2])
    # 시간순으로 정렬
    plans.sort(key=lambda x: x[1])
    stack = []
    for i,p in enumerate(plans):
        j,s,c = p
        # 마지막 과제가 아니라면
        if i != len(plans)-1:
            nxt_s = plans[i+1][1]
            remain = nxt_s - s
        else:
            remain = float('inf')
        
        if remain >= c:
            ans.append(j)
            remain -= c
            while stack and remain > 0:
                lst_j,lst_remain = stack.pop()
                if remain >= lst_remain:
                    ans.append(lst_j)
                    remain -= lst_remain
                else:
                    stack.append((lst_j,lst_remain-remain))
                    remain -= lst_remain
        else:
            stack.append((j,c-remain))
    while stack:
        ans.append(stack.pop()[0])
    return ans