#개미 전사
#일직선상에 존재하는 식량창고를 약탈한다.
#인접한 식량창고를 약탈한다면 발각된다.
#들키지 않고 약탈하기 위해서는 한칸이상 떨어진 식량창고를 공략해야 한다.
#들키지 않고 얻을 수 있는 최대한의 식량을 구하라.

import sys

def deprive(n, array):
    dp_table = [0]*n
    if n > 1:
        dp_table[0] = array[0]
        dp_table[1] = max(array[0], array[1])
    else : 
        print("Error!")
        return 0

    for i in range(2, n):
        dp_table[i] = max(dp_table[i-1], dp_table[i-2] + array[i])

    return dp_table[-1]

if __name__ == '__main__':
    warehouseNum = int(sys.stdin.readline())
    food = list(map(int, sys.stdin.readline().split()))

    print(deprive(warehouseNum, food))

