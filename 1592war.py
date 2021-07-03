import sys

def creat_ans(ans_str, ans_len):
    ans = []
    for i in range(ans_len):
        for j in range(i+1, ans_len):
            ans.append([ans_str[i], ans_str[j]])
    return ans

num = int(sys.stdin.readline())
cor = list(sys.stdin.readline().split())
ans = list(sys.stdin.readline().split())
count = 0

cor_zip = creat_ans(cor, num)
ans_zip = creat_ans(ans, num)

for i in ans_zip:
    if i in cor_zip:
        count += 1
print("{0}/{1}".format(count, len(cor_zip)))
