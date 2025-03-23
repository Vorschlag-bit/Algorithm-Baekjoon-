from itertools import product as perm
def solution(users, es):
    # 완전탐색으로 하면, 40 ^ len(es)
    # 특정 이모티콘이 현재 n% 할인임을 기록하면서 다른 이모티콘의 할인을 적용한 걸 계산해야 함
    # 최대의 목표를 달성하기 위한 답 => 최대의 할인율 중 최소의 할인율을 찾기
    # 모든 이모티콘마다 최대의 할인율 중 최소의 할인율을 찾아야 한다.
    # 특정 이모티콘의 할인율은 다른 이모티콘의 할인율에 영향을 끼침
    # 데카르트의 곱을 사용해서 모든 수 고려, 이모티콘 1 - n까지 1-40으로 만들 수 있는 경우의 수
    ans = [0,0]
    dis = [10,20,30,40]
    for discount in perm(dis, repeat=len(es)):
        # [10,10] ~ [40,40]
        # 원본 가격 배열 복사
        emos = []
        # 할인 적용
        for idx, price in enumerate(es):
            dis_price = price * (100 - discount[idx]) // 100
            emos.append(dis_price)
        # 가입자 수
        mem = 0
        # 총 구매금액
        total = 0
        for user_h,user_m in users:
            # 총 구매량
            amount = 0
            for idx in range(len(discount)):
                # 멤버 기준이상이면 구매
                if discount[idx] >= user_h:
                    amount += emos[idx]
            if amount >= user_m:
                mem += 1
            else:
                total += amount
        # 최대 판별
        if mem > ans[0] or (mem == ans[0] and total > ans[1]):
            ans = [mem,total]
    return ans
