from itertools import product as perm
def solution(users, emoticons):
    # 임티플 최대 가입 수, 최대 매출액
    ans = [0,0]
    # 10,20,30,40을 len(emo)만큼 중복순열로 뽑기
    discount = [10,20,30,40]
    for dis in perm(discount, repeat=len(emoticons)):
        # 이모티콘 별로 적용할 할인율 설정
        plus = 0
        total = 0
        for user_ratio,user_limit in users:
            # 유저마다 구매 판별
            amount = 0
            for idx,price in enumerate(emoticons):
                ratio = dis[idx]
                if ratio >= user_ratio:
                    # 할인 적용한 가격
                    amount += price - ((price * ratio) // 100)
                if amount >= user_limit:
                    plus += 1
                    amount = 0
                    break
            total += amount
        if ans[0] < plus or (ans[0] == plus and ans[1] < total):
            ans[0] = plus
            ans[1] = total
    return ans