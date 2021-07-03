import sys
def hansoo(num):
    count = 0
    if num >= 1000:
        return 0
    a = int(num/100) 
    b = int((num-(a*100))/10) 
    c = int(num-(a*100)-(b*10))
    
    if a == 0 and b == 0:
        count = 1
    elif a == 0:
        count = 1
    else:
        if (c-b) == (b-a):
            count = 1
    #print(a, b, c, count)
    return count

count = 0
n = int(sys.stdin.readline())
for i in range(1,n+1):
    count += hansoo(i)
print(count)