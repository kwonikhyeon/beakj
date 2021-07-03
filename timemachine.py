import sys
count = 0
time = sys.stdin.readline().strip().split(":")

for i in range(3):
    print(len(time[i]))






'''
for i in range(3):
    if len(time[i]) == 2:
        if 1 <= int(time[i]) <= 12:
            if 0 <= int(time[i+1]) <= 59 and 0 <= int(time[i-1]) <= 59:
                count += 2
print(count)
'''