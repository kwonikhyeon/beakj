#효율적인 화폐 구성
#N가지 종류의 화폐를 정의
#M원을 N가지 종류의 화폐로 구성
#구성이 같고 순서가 다르면 같은 것으로 구분

import sys

def cashing(n_list, m):
    dp_table = [10001]*(m+1)
    dp_table[0] = 0

    for i in range(len(n_list)):
        for j in range(m+1):
            if j % n_list[i] == 0:
                dp_table[j] = min(dp_table[j], j//n_list[i])

    if dp_table[-1] == 10001:
        end_num = []
        for i in range(len(n_list)):
            end_num.append(dp_table[-1-i]+1)

        dp_table[-1] = min(end_num)

    if dp_table[-1] >= 10001: return -1
    
    return dp_table[-1]

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    n_list = [int(sys.stdin.readline()) for _ in range(n)]

    print(cashing(n_list, m))
    