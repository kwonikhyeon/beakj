import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, (heapq.heappop(scoville))+2*(heapq.heappop(scoville)))
            print(scoville)
        except IndexError:
            return -1
        answer += 1    
    return answer

s = [5, 2, 4, 9, 6, 3, 5, 7, 12, 65, 24, 18]
re = solution(s, 20)
print(re)
