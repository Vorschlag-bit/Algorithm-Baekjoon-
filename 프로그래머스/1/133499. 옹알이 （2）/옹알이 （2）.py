def solution(b):
    dic = {"aya":"1","ye":"2","woo":"3","ma":"4"}
    ans = 0
    arr = []
    for word in b:
        for k in dic.keys():
            word = word.replace(k,dic[k])
        arr.append(word)
    for word in arr:
        char = '.'
        flag = True
        for c in word:
            if not c.isdigit() or c == char:
                flag = False
                break
            char = c
        if flag: ans += 1
    return ans