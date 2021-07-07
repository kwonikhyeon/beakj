def solution(numbers):
    answer = ''
    numbers = sorted(list(map(str,numbers)),key=lambda x : x*3 ,reverse=True)
    for i in range(len(numbers)): answer = answer+numbers[i]
    return str(int(answer))

numbers = [3,30,34,5,9]
print(solution(numbers))
