def solution(words):
    ans = 0
    words.sort()
    for i in range(len(words)):
        cur = words[i]
        # 가장 많이 겹치는 prefix 길이
        overlap = 0
        # 1이상일 경우 이전 문자열과 비교
        if i > 0:
            prev = words[i-1]
            cnt = 0
            for j in range(min(len(prev),len(cur))):
                if cur[j] == prev[j]: cnt += 1
                else: break
            overlap = max(overlap, cnt)
        
        # 마지막 문자 전까지 이후 문자열과 비교
        if i < len(words) - 1:
            nxt = words[i+1]
            cnt = 0
            for j in range(min(len(nxt),len(cur))):
                if cur[j] == nxt[j]: cnt += 1
                else: break
            overlap = max(overlap, cnt)
        # 최대한 겹치는 것보다 1만큼 더 입력하면 최소 구분자 개수
        overlap += 1
        ans += min(overlap, len(words[i]))
    return ans