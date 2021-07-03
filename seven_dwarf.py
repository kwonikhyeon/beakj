##7난쟁이 키의 합이 100, 숨어있는 난쟁이 2명 찾기
import sys
dwarfs = [0] * 9
save = 0
for i in range(9):
    dwarfs[i] = int(sys.stdin.readline())
dwarfs.sort()
for i in range(9):
    save = dwarfs[i]
    dwarfs.remove(save)
    for j in dwarfs:
        if save + j == sum(dwarfs) + save - 100:
            n1, n2 = save, j
    dwarfs.append(save)
    dwarfs.sort()
dwarfs.remove(n1)
dwarfs.remove(n2)
for i in range(7):
    print(dwarfs[i])
