from collections import defaultdict
from itertools import combinations as comb
from bisect import bisect_left
def solution(infos, querys):
    db = defaultdict(list)
    ans = []
    # 아이디어 => 지원자의 조건에 맞는 16가지 경우의 수를 key로 점수list를 value로
    for info in infos:
        # 리스트화
        info = info.split()
        # 점수
        score = int(info[-1])
        info = info[:4]
        for i in range(5):
            for case in comb([0,1,2,3],i):
                # 조합으로 만들어진 인덱스의 값만 '-'로 바꾸기
                temp = info[:]
                for c in case:
                    temp[c] = '-'
                key = ''.join(temp)
                db[key].append(score)
    # 미리 정렬
    for item in db:
        db[item].sort()
    # query를 돌면서 점수 이진탐색으로 찾기
    for query in querys:
        q = query.replace("and ", "").split()
        condition = ''.join(q[:4])
        score = int(q[-1])
        arr = db[condition]
        idx = bisect_left(arr,score)
        ans.append(len(arr) - idx)
    return ans