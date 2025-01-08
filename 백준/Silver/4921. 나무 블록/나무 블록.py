import sys

def check(num, idx):
    match int(num[idx]):
        case 1:
            if (int(num[idx + 1]) != 4 and int(num[idx + 1]) != 5) or idx != 0:
                return False
            return True
        case 2:
            if idx != len(num) - 1:
                return False
            return True
        case 3:
            if int(num[idx + 1]) != 4 and int(num[idx + 1]) != 5:
                return False
            return True
        case 4:
            if int(num[idx + 1]) != 2 and int(num[idx + 1]) != 3:
                return False
            return True
        case 5:
            if int(num[idx + 1]) != 8:
                return False
            return True
        case 6:
            if int(num[idx + 1]) != 2 and int(num[idx + 1]) != 3:
                return False
            return True
        case 7:
            if int(num[idx + 1]) != 8:
                return False
            return True
        case 8:
            if int(num[idx + 1]) != 7 and int(num[idx + 1]) != 6:
                return False
            return True

no = 1
while True:
    cases = sys.stdin.readline().strip()
    if int(cases) == 0:
        break
    # 처음은 반드시 1 끝은 반드시 2
    if int(cases[0]) != 1 or int(cases[len(cases) - 1]) != 2:
        print(f"{no}. NOT")
        no += 1
        continue
    # case 완전 탐색
    for i in range(len(cases)):
        if not check(cases, i):
            print(f"{no}. NOT")
            no += 1
            break
    else:
        print(f"{no}. VALID")
        no += 1
