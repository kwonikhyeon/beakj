def solution(numbers, target):
    sup= [0]
    for i in numbers:
        sub = []
        for j in sup : 
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
        print(sup)
    return sup.count(target)

n = [1,1,1,1,1]
t = 3

print(solution(n,t))