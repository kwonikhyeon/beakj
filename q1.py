def solution(progresses, speeds):
    answer = []
    c = 0
    while True:
        if progresses == []: break
        for i in range(len(progresses)):
            if progresses[i] < 100: progresses[i] = progresses[i] + speeds[i]
        print(progresses)
        while True:
            if progresses[0] < 100: break
            else:
                del progresses[0]
                c += 1
        answer.append(c)

    return answer

p = [93, 30, 55]
s = [1, 30, 5]
o = []
solution(p, s)

