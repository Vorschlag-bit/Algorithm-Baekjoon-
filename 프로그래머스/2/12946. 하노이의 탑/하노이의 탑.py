def solution(n):
    ans = []
    # 전체 문제를 더 작은 문제로 쪼개기
    # 1. n-1개의 원판을 보조 기둥(2번)으로 옮기기
    # 2. n번째 원판을 3번으로 옮기기
    # 3. n-1개의 원판을 2번에서 3번으로 옮기기
    def h(n, fr, to, via):
        # 종료조건, n == 1이면 to으로 옮기고 return
        if n == 1:
            ans.append([fr,to])
            return
        h(n-1, fr, via, to)
        print(f"{fr} to {to} via {via}")
        ans.append([fr,to])
        h(n-1, via, to, fr)
    h(n,1,3,2)
    return ans