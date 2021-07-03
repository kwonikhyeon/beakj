##심박수로 운동, 휴식 결정하는 코드
import sys
N, m, M, T, R = map(int, sys.stdin.readline().split())
pulse = m
n_E = 0
n_R = 0
while n_E < N:
    if M - pulse >= T:
        n_E += 1
        pulse += T
    else:
        n_R += 1
        if pulse - R < m:
            pulse = m
        else:
            pulse -= R
print(n_E + n_R)