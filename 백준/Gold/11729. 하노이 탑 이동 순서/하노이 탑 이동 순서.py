# n - 1번째 원판을 옮길 수 있다면 n번째 원판도 옮길 수 있다.

num = int(input())
# a에서 b로 n개의 원판을 옮기는 재귀
def hanoi(a, b, n):
    if n == 1:
        print(str(a) + " " + str(b))
        return
    # a에서 6-a-b로 n-1 개의 원판을 옮겨야 함
    hanoi(a, 6-a-b, n-1)
    print(str(a) + " " + str(b))
    hanoi(6-a-b, b, n-1)
print(2 ** num -1)
hanoi(1, 3, num)
    
