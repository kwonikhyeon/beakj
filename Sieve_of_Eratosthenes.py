##에라토스테네스의 체-N숫자 안의 수 중 c번째로 삭제되는
##값 출력하기
import sys
N, c = map(int, sys.stdin.readline().split())
a = list(range(2,N+1))
d = list(range(2,N+1))
count = 0
for i in d:
    for j in range(1, int(a[-1]/i)+1):
        if i*j in a:
            a.remove(i*j)
            b = i*j
            count += 1
            if count == c:
                break
    if count == c:
                break
print(b)
