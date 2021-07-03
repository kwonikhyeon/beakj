##산술평균, 중앙값, 최빈값, 범위 구하기(2108번)
import sys
import numpy as np
def mode(list_):
    return max(list_, key=list_.count)


num = int(sys.stdin.readline())

value = []
for i in range(num):
    value.append(int(sys.stdin.readline()))

print(round(np.mean(value)))
print(int(np.median(value)))
print(mode(value))
print(max(value) - min(value))


    