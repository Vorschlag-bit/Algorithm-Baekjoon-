def solution(keymap, targets):
    ans = []
    for t in targets:
        if len(set(t) - set(list(''.join(keymap)))): ans.append(-1)
        else:
            cnt = 0
            for char in t:
                chr_min = min(k.index(char)+1 for k in keymap if char in k)
                cnt += chr_min
            ans.append(cnt)
    return ans