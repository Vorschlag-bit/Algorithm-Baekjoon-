dic = {"A#":"a","B#":"b","C#":"c","D#":"d","E#":"e","F#":"f","G#":"g"}
def solution(m, infos):
    ans = []
    for i in infos:
        st,et,title,melody = i.split(',')
        start = st.split(':')
        end = et.split(':')
        time = 60 * (int(end[0]) - int(start[0]))
        time += int(end[1]) - int(start[1])
        # 멜로디 수정
        for k in dic.keys():
            melody = melody.replace(k,dic[k])
            m = m.replace(k,dic[k])
        lyric = (melody * (time // len(melody))) + melody[:(time%len(melody))]
        if m in lyric:
            ans.append((time, title))
    if ans:
        return sorted(ans, key=lambda x: -x[0])[0][1]
    else:
        return '(None)'
    