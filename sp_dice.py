##주사위 3개의 면 수를 지정하고 던져서 나오는 각 수를 더했을때
##가장 많이나오는 수 도출하는 코드
import sys
a = []
s1, s2, s3 = map(int, sys.stdin.readline().split())
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            a.append(i + j + k)
print(max(a, key=a.count))