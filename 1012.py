import sys
sys.setrecursionlimit(100000)

def check(m,n,k,l):
    if [k+1,l] in p: check(m,n,k+1,l)
    elif [k-1,l] in p: check(m,n,k-1,l)
    elif [k,l+1] in p: check(m,n,k,l+1)
    elif [k,l-1] in p: check(m,n,k,l-1)

    p.remove([k,l])



p=[]
num = int(sys.stdin.readline())
jirung1 = [0]*num
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    for j in range(c):
        p.append(list(map(int, sys.stdin.readline().split())))
    for k in range(m):
        for l in range(n):
            if [k,l] in p: 
                check(m,n,k,l)
                jirung1[i] += 1

for i in range(num): print(jirung1[i])
                
