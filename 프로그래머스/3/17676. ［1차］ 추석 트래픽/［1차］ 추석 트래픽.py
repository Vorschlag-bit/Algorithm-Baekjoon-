def t2ms(t):
    s = t.split()
    h,m,sec = s[1].split(":")
    second = int(sec.split(".")[0])*1000
    ms = int(sec.split(".")[1])
    end = int(h)*60*60*1000+int(m)*60*1000+second+ms
    dur = float(s[2][:-1])*1000
    start = end - int(dur) + 1
    return (start,end)
def solution(lines):
    ans = 0
    arr = [t2ms(l) for l in lines]
    ts = []
    for s,e in arr:
        ts.append(s)
        ts.append(e)
    for t in ts:
        te = t + 1000
        cnt = sum(1 for s,e in arr if e >= t and s < te)
        ans = max(cnt,ans)
    return ans