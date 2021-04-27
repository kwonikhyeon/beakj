import sys
from collections import Counter
N, M = map(int,sys.stdin.readline().split())
DNA = [0]*N
DNA_index = []
D = [0]*M
New = [0]*M
count = 0
for i in range(N):
    DNA[i] = list(sys.stdin.readline().rstrip())
for i in range(M):
    line = []
    for j in range(N):
        line.append(list(DNA[j][i]))
    DNA_index.append(line)
for i in range(M):
    D[i] = "".join(sum(DNA_index[i], []))

for i in range(M):
    c = Counter(D[i]).most_common(n = 4)
    c_sort = sorted(c, key=lambda x : (-x[1], x[0]))
    New[i] = c_sort[0][0]


for i in range(N):
    for j in range(M):
        if DNA[i][j] != New[j]:
            count += 1


H_DNA = ''.join(New)
print(H_DNA)
print(count)
