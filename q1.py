def solution(progresses, speeds):
    answer = []
    while True:
        c = 0
        if progresses == []: break
        for i in range(len(progresses)):
            if progresses[i] < 100: progresses[i] += speeds[i]
        while True:
            if progresses == [] or progresses[0] < 100: break
            else:
                del progresses[0]
                c += 1
        if c != 0: answer.append(c)
    return answer

p = [0,0,0,0]
s = [10,8,2,15]
o = []
print(solution(p, s))

