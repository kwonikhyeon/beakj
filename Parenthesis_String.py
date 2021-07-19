import sys

num = int(sys.stdin.readline())
a = []
for _ in range(num):
    str = list(sys.stdin.readline().strip())
    cnt = 0
    for i in range(len(str)):
        if str[i] == '(': cnt += 1
        elif str[i] == ')': cnt -= 1
        else:
            ans = "NO"
            break
        if cnt < 0:
            ans = "NO"
            break
        elif i == len(str)-1:
            if cnt == 0: ans = "YES"
            else: ans = "NO"
            break    
    a.append(ans)

for j in range(num): print(a[j])