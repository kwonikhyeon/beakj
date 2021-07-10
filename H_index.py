def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i: return len(citations)-i
    return 0

c = [4,5,5,6,7,2,1]
print(solution(c))
    