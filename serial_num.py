import sys
num = int(sys.stdin.readline())
data = []
for _ in range(num):
    add_num = 0
    alpha = sys.stdin.readline().rstrip()
    for i in alpha:
        if i.isdigit():
            add_num += int(i)
    data.append((alpha, add_num))

data.sort(key=lambda x : (len(x[0]), x[1], x[0]))

for i in data:
    print(i[0])