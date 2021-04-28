import sys
'''재귀함수
sys.setrecursionlimit(10**6)
def Fibo(n):
    if n == 1 or n ==2:
        return 1
    else:
        return Fibo(n-2) + Fibo(n-1)

num = int(sys.stdin.readline())
print(Fibo(num))
'''
num = int(sys.stdin.readline())
f = [0, 1, 1]
for i in range(3, num + 1):
    f.append(f[i - 1] + f[i - 2])
print(f[num])