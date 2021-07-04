import sys
sys.setrecursionlimit(10**6)

def check(y,x):
    if x < 0 or y < 0 or x > n or y > m:
        return
    if p[y][x] == 0:
        return

    p[y][x] == 0
    check(y,x+1)
    check(y,x-1)
    check(y+1,x)
    check(y-1,x)


num = int(sys.stdin.readline())
jirung = [0]*num
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    p = [[0]*m for _ in range(n)]
    for _ in range(c):
        a,b = map(int,sys.stdin.readline().split())
        p[b][a] = 1

    for u in range(n):
        for v in range(m):
            print(p[u][v], end='')
        print("")

    print('\n')

    for k in range(n):
        for l in range(m):
            if p[k][l] == 1:
                check(k,l)
                jirung[i] += 1
            print(p[k][l], end='')
        print("")

#print(jirung[i] for i in range(num))
