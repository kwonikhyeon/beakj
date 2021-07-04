import sys

def game(s, n, p):
    p += s[n]
    if s[n-1] > s[n-2]:
        p += s[n-1]
        n = n-3
        game(s,n,p)
    elif s[n-1] == s[n-2]:
        p += s[n-1]
        n = n-1
        game(s,n,p)
    else:
        n = n-2
        game(s,n,p)

    return p

num = int(sys.stdin.readline())
stairs = []
for i in range(num): stairs.append(int(sys.stdin.readline()))
point = 0
print(game(stairs,num-1,point))
