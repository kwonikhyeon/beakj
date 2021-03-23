##치킨쿠폰, 도장 k개당 쿠폰 1개
import sys
while 1:
    try:
        stamp = 0
        answer = 0
        n, k = map(int, sys.stdin.readline().split())
        answer += n
        stamp += n
        while stamp >= k:
            n = stamp // k
            answer += n
            stamp = stamp % k + n
    except:
        break
    print(answer)