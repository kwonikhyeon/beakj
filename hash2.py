def solution(phone_book):
    answer = True
    hash = {}
    nn = sorted(phone_book)
    for i in range(len(nn)-1):
        if len(nn[i]) < len(nn[i+1]):
            if nn[i+1].startswith(nn[i]):
                answer = False
                break  
    return answer

n = ["119", "87674223", "1195524421", "9"]
print(solution(n))
