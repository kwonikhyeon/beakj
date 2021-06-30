import sys

def check(m,n,po,o):
    if (o[0]+1,o[1]) in po: 
        po.remove(o[0]+1,o[1])
        check(m,n,po,(o[0]+1,o[1]))
    elif (o[0]-1,o[1]) in po: 
        check(m,n,po,(o[0]-1,o[1]))
    elif (o[0],o[1]+1) in po: 
        check(m,n,po,(o[0],o[1]+1))
    elif (o[0],o[1]-1) in po: 
        check(m,n,po,(o[0],o[1]-1))


jirung1 = 0 
jirung2 = 0
p=[]
num = int(sys.stdin.readline())
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    for j in range(c):
        p.append(list(map(int, sys.stdin.readline().split())))
    for k in range(m):
        for l in range(n):
            if (k,l) in p: check(m,n,p,(k,l))
                
