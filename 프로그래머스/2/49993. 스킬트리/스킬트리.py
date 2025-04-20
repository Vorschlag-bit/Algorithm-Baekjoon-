def solution(skill, stree):
    ans = []
    for st in stree:
        seq = []
        for char in skill:
            if char not in st:
                idx = 27
            else: idx = st.index(char)
            seq.append(idx)
        flag = True
        for i in range(1,len(seq)):
            ex = seq[i-1]
            cur = seq[i]
            if cur < ex:
                flag = False
                break
        if flag: ans.append(1)
    return len(ans)