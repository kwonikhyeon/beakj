
import sys

def check(k,l):
    if [k+1,l] in p: check(k+1,l)
    elif [k-1,l] in p: check(k-1,l)
    elif [k,l+1] in p: check(k,l+1)
    elif [k,l-1] in p: check(k,l-1)

    p.remove([k,l])
'''
p=[]
num = int(sys.stdin.readline())
jirung = [0]*num
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    for j in range(c):
        p.append(list(map(int, sys.stdin.readline().split())))
    for k in range(m):
        for l in range(n):
            if [k,l] in p: 
                #check(k,l)
                jirung[i] += 1
    p.clear()

for i in range(num): print(jirung[i])
'''

num = int(sys.stdin.readline())
jirung = [0]*num
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    p = [[0]*m for i in range(n)]
    for j in range(c):
        a,b = int(sys.stdin.readline().split())
        p[b][a] = 1
    