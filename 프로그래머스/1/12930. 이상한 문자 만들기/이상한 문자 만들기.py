def solution(s):
    arr = []
    p = 0
    for i,c in enumerate(s):
        if s[i] == ' ':
            p = 0
            arr.append(s[i])
        else:
            if p % 2 == 0: arr.append(s[i].upper())
            else: arr.append(s[i].lower())
            p += 1
    return ''.join(arr)