def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        if completion[i] in participant: participant.remove(completion[i])
    answer = participant[0]
    return answer

def solution2(participant, completion):
    hash = {}
    answer = ''
    for i in participant:
        if i in hash: hash[i] += 1
        else: hash[i] = 1
    for j in completion:
        if hash[j] == 1: del hash[j]
        else: hash[j] -= 1
    answer = list(hash.keys())[0]
    return answer



p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

print(solution2(p,c))