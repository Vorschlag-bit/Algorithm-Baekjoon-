def solution(files):
    ans = []
    d = []
    for idx,file in enumerate(files):
        # lower로 head 소문자화
        low = file.lower()
        num_s, num_e = 0,0
        head = ''
        for i,char in enumerate(low):
            if char.isdigit():
                num_s = i
                break
            head += char
        for i in range(num_s,len(low)):
            if low[i].isdigit():
                num_e = i
            else: break
        num = int(low[num_s:num_e+1])
        # head, num ,idx
        d.append((head,num,idx))
    d.sort(key=lambda x: (x[0],x[1]))
    for h,n,idx in d:
        ans.append(files[idx])
    return ans