def solution(record):
    ans = []
    nick = dict()
    # 닉네임 기록
    for rec in record:
        commands = rec.split()
        if commands[0] == 'Enter':
            nick[commands[1]] = commands[2]
        if commands[0] == 'Change':
            nick[commands[1]] = commands[2]
            
    for rec in record:
        coms = rec.split()
        if coms[0] == 'Enter':
            ans.append(f"{nick[coms[1]]}님이 들어왔습니다.")
        elif coms[0] == 'Leave':
            ans.append(f"{nick[coms[1]]}님이 나갔습니다.")
        else:
            continue
    
    return ans