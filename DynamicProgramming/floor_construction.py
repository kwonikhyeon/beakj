#바닥공사
#가로 길이 N, 세로 길이 2인 직사각형을
#1*2, 2*1, 2*2의 덮개로 채우는 경우의 수 구하기
#결과는 796,796으로 나눈 값을 가진다(큰 수 방지)

import sys

def construction(n):
    dpArr = [0]*n
    if n < 1: 
        print("Error")
        return 0

    dpArr[0] = 1 
    dpArr[1] = 3

    for i in range(2,n):
        dpArr[i] = dpArr[i-1] + 2*dpArr[i-2]

    return dpArr[n-1]%796796

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(construction(n))