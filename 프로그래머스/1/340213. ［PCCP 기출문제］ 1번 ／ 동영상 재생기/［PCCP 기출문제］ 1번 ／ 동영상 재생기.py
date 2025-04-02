def solution(video_len, pos, op_start, op_end, commands):
    ans = ''
    # 모두 초 단위로 바꾸기
    def tosec(string):
        mm,ss = string.split(":")
        return int(mm) * 60 + int(ss)
    ops = tosec(op_start)
    ope = tosec(op_end)
    v_len = tosec(video_len)
    sec = tosec(pos)
    if ops <= sec <= ope:
            sec = ope
    for cmd in commands:
        if cmd == "next":
            if sec + 10 > v_len:
                sec = v_len
            else:
                sec += 10
        elif cmd == "prev":
            if sec - 10 < 0:
                sec = 0
            else:
                sec -= 10
        if ops <= sec <= ope:
            sec = ope
    m = str(sec // 60)
    m = m.rjust(2,'0')
    s = str(sec % 60)
    s = s.rjust(2,'0')
    return m+":"+s