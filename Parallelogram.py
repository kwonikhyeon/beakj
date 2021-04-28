import math, sys
def P_L(x,y,x1,y1,x2,y2):
    v1 = [x1 - x, y1 - y]
    v2 = [x2 - x, y2 - y]
    if v1[1]/v1[0] == v2[1]/v2[0]:
        return -1
    else:    
        L = 2*(math.sqrt(v1[0]**2+v1[1]**2) + math.sqrt(v2[0]**2+v2[1]**2))
        return L

ax, ay, bx, by, cx, cy = map(int,sys.stdin.readline().split())
a_l = P_L(ax, ay, bx, by, cx, cy)
b_l = P_L(bx, by, ax, ay, cx, cy)
c_l = P_L(cx, cy, bx, by, ax, ay)
length = [a_l, b_l, c_l]
if length[0] == length[1] == length[2] == -1:
    print("-1.0")
else:
    minus = max(length) - min(length)
    print(minus)
