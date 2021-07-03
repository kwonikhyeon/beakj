##주차장 요금
import sys
f_1, f_2, f_3 = map(int, sys.stdin.readline().split())
time = [0] * 3
for i in range(3):
    time[i] = list(map(int, sys.stdin.readline().split()))
    time[i] = list(map(int, range(time[i][0]+1, time[i][1]+1)))
during = max(map(max, time))
compare = list(range(1,during+1))
add = [0]*during
for i in range(during):
    for j in range(3):
        add[i] += time[j].count(compare[i])
    if add[i] == 1:
        add[i] = 1 * f_1
    elif add[i] == 2:
        add[i] = 2 * f_2
    elif add[i] == 3:
        add[i] = 3 * f_3
print(sum(add))