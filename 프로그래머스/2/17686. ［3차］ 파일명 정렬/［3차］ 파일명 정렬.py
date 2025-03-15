def solution(f):
    # head는 대소문자를 구분않는 사전 순
    # head가 똑같을 경우, num 오름차순(0무시)
    # num까지 같다면 그냥 들어온 순서대로
    ans = []
    fs = []
    for file in f:
        lowfile = file.lower()
        head = ''
        for i in lowfile:
            if i.isdigit():
                break
            head += i
        ns = 0
        for i in file:
            if i.isdigit():
                ns = file.index(i)
                break
        l = 0
        for i in range(ns, len(file)):
            if not file[i].isdigit():
                break
            l += 1
        num = int(file[ns:ns+l])
        print(num)
        fs.append((head,num,file))
    fs = sorted(fs, key=lambda x: (x[0],x[1]))
    for f in fs:
        ans.append(f[2]) 
    return ans