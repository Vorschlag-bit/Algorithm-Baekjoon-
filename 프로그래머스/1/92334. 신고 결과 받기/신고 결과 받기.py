def solution(id_list, report, k):
    ans = []
    banned = set()
    # 신고한 사람
    reporter = dict()
    # 신고된 사람
    reported = dict()
    # 유저 등록
    for user in id_list:
        reported[user] = set()
        reporter[user] = set()
    # 신고 시작
    for log in report:
        u1,u2 = log.split()
        reported[u2].add(u1)
        reporter[u1].add(u2)
    # bann 리스트 갱신
    for user in id_list:
        if len(reported[user]) >= k:
            banned.add(user)
    # 메일 횟수
    for user in id_list:
        cnt = 0
        reported_users = reporter[user]
        for rep_user in reported_users:
            if rep_user in banned:
                cnt += 1
        ans.append(cnt)
    
    return ans