def solution(mats, park):
    mats.sort(reverse=True)
    n = len(park)
    m = len(park[0])
    
    def check(x,y,l):
        for i in range(x,x+l):
            for j in range(y,y+l):
                if park[i][j] != "-1":
                    return False
        return True
    
    for mat in mats:
        for i in range(n-mat+1):
            for j in range(m-mat+1):
                if check(i,j,mat):
                    return mat
    return -1