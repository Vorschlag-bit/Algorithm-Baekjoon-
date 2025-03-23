from collections import deque
def solution(queue1, queue2):
    t = 0
    imp = 0
    s1 = 0
    s2 = 0
    q1 = deque()
    q2 = deque()
    for n in queue1:
        q1.append(n)
        t += n
        imp += 1
        s1 += n
    for n in queue2:
        q2.append(n)
        t += n
        imp += 1
        s2 += n
    t //= 2
    ans = 0
    # 절대 같게 못 만들면 -1 출력
    # 한 큐에서 꺼내서 다른 큐로 넣기
    # 서로 한 바퀴씩 돌았을 때, 같게 못 만들면... -1 출력
    # 한 큐를 t가 될 때까지 쭉 반복하는데,
    # q1 = [2,2], q2 = [3,5]
    # q1 = [2,2,3], q2 = [5]
    # q1 = [2,3], q2 = [5,2]
    # q1 = [2,3,5], q2 = [2]
    # q1에 모든 원소가 들어갔다가 나온 적이 있으면, 불가능한 숫자
    # q1에 들어간 적이 있는 모든 원소 개수 변수를 설정 후, 배열의 길이가 모든 원소의 배열의 길이가
    # 모든 원소 길이와 같아지면 break
    # 당연히 합이 큰 q에서 빼서 작은 쪽으로 넣는다, 같게 만들기 위해 빼다가 q가 비면 false
    l = len(q1)
    while True:
        if s1 == s2:
            return ans
        if l == imp:
            return -1
        # 더 큰 쪽에서 빼서 작은 쪽으로 담기
        if s2 > s1:
            num = q2.popleft()
            s1 += num
            s2 -= num
            q1.append(num)
            l += 1
            ans += 1
        elif s1 > s2:
            num = q1.popleft()
            s1 -= num
            s2 += num
            q2.append(num)
            ans += 1