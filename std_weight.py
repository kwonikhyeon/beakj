##표준몸무게 구하기
import sys
def std_weight (height, gender):
    if gender == '남자':
        print(format(height * height * 22,".2f"))
    elif gender == '여자':
        print(format(height * height * 21,".2f"))

h, s = sys.stdin.readline().split()
h = float(h) / 100
std_weight(h, s)