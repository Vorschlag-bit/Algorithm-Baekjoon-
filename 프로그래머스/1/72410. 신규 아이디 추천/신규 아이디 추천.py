def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    dic = []
    # a-z
    for i in range(26):
        dic.append(chr(ord('a') + i))
    # 0-9
    for i in range(10):
        dic.append(str(i))
    # -,_,.
    dic.append('-')
    dic.append('_')
    dic.append('.')
    t = new_id
    for char in new_id:
        if char not in dic:
            t = t.replace(char, '')
    new_id = t
    prevchar = ''
    result = ''
    for char in new_id:
        if char == '.' and prevchar == '.':
            continue
        result += char
        prevchar = char
    if len(result) > 0 and result[0] == '.': result = result[1:]
    if len(result) > 0 and result[-1] == '.': result = result[:len(result)-1]
    if len(result) == 0: result = "a"
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:len(result) - 1]
    elif len(result) <= 2:
        while len(result) < 3:
            result = result + result[-1]
    return result