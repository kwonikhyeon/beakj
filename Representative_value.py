##10개의 숫자 중 대표값(평균값&최빈값)구하는 코드
import sys
a = [0]*10
for i in range(10):
    a[i] = int(sys.stdin.readline())
    
print(sum(a)//10)
print(max(a, key=a.count))##max를 이용한 최빈값 도출하는 식