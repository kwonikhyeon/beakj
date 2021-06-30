import sys

a, b = map(int, sys.stdin.readline().split())
L, R = 0, 0

while True:
    if a==1: 
        R+=(b-1)
        break
    elif b==1:
        L+=(a-1)
        break
    if a>b:
        L+=int(a/b)
        a%=b
    else:
        R+=int(b/a)
        b%=a

print(L, R)