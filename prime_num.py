##숫자 갯수 입력 후 갯수만큼 수 넣으면 소수 갯수 출력
import sys
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    if num[i] == 1:
        num[i] = 0
    elif num[i] == 2:
        num[i] = 1
    elif num[i] > 2:
        for j in range(2,num[i]):
            if num[i] % j == 0:
                num[i] = 0
                break
print(len(num) - num.count(0))