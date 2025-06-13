def solution(people, limit):
    ans = 0
    # 한번에 최대 2명
    people.sort()
    # 어떤 사람을 고를 때 함께 탈 수 있는지 없는지 판단하는 방법
    i,j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        ans += 1
    return ans