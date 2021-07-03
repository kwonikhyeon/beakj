##N팩토리얼에서 끝자리에 나오는 0 갯수 구하기
import sys
N = int(sys.stdin.readline())
P_N = 1
count = 0
for i in range(1, N+1):
    P_N = P_N * i
P_N = str(P_N)
for i in reversed(range(len(P_N))):
    if P_N[i] == '0':
        count += 1
    else:
        break
print(count)
    

