import sys

jirung1, jirung2 = 0
p=[]
num = int(sys.stdin.readline())
for i in range(num):
    m, n, c = map(int, sys.stdin.readline().split())
    for j in range(c):
        p.append(list(map(int, sys.stdin.readline().split())))

