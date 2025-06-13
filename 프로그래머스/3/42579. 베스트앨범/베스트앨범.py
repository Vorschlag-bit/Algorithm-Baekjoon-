from collections import Counter,defaultdict
def solution(genres, plays):
    ans = []
    total = dict()
    g_cnt = defaultdict(list)
    for i,g in enumerate(genres):
        total[g] = total.get(g,0) + plays[i]
        g_cnt[g].append((i,plays[i]))
    # 많이 재생된 장르부터
    items = sorted(total.items(), key=lambda x: x[1], reverse=True)
    for k,v in items:
        # 재생 수 내림차순, idx 오름차순
        sorted_cnt = sorted(g_cnt[k], key=lambda x: (-x[1],x[0]))
        ans.append(sorted_cnt[0][0])
        if len(sorted_cnt) > 1:
            ans.append(sorted_cnt[1][0])
    return ans