from copy import deepcopy


def findMisplacedTiles(a, b):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if a[i][j] != b[i][j]:
                cnt += 1
    return cnt


def makeLeft(a, b, c):
    a[b][c], a[b][c-1] = a[b][c-1], a[b][c]
    return a


def makeRight(a, b, c):
    a[b][c], a[b][c+1] = a[b][c+1], a[b][c]
    return a


def makeUp(a, b, c):
    a[b][c], a[b-1][c] = a[b-1][c], a[b][c]
    return a


def makeDown(a, b, c):
    a[b][c], a[b+1][c] = a[b+1][c], a[b][c]
    return a


prb = [[1, 2, 3], [5,6,0], [7,8,4]]
sol = [[1,2,3], [5,8,6], [0,7,4]]
cnt = findMisplacedTiles(sol, prb)
c = 0
for i in prb:
    print(i)
print()

while True:
    if cnt == 0:
        break
    else:
        i1 = i2 = 0
        t1 = t2 = t3 = t4 = 10
        t_left = t_right = t_up = t_down = []
        for i in range(3):
            for j in range(3):
                if prb[i][j] == 0:
                    i1, i2 = i, j
        if(i1-1 != -1):
            temp = deepcopy(prb)
            t_up = makeUp(temp, i1, i2)
            t1 = findMisplacedTiles(sol, t_up)
        if(i2-1 != -1):
            temp = deepcopy(prb)
            t_left = makeLeft(temp, i1, i2)
            t3 = findMisplacedTiles(sol, t_left)
        if(i1+1 != 3):
            temp = deepcopy(prb) 
            t_down = makeDown(temp, i1, i2)
            t2 = findMisplacedTiles(sol, t_down)
        if(i2+1 != 3):
            temp = deepcopy(prb)
            t_right = makeRight(temp, i1, i2)
            t4 = findMisplacedTiles(sol, t_right)

        f = min(t1, t2, t3, t4)
        if f == t1:
            prb = t_up
        if f == t2:
            prb = t_down
        if f == t3:
            prb = t_left
        if f == t4:
            prb = t_right
        for i in prb:
            print(i)
        print()
        if sol == prb:
            break
print("success")
