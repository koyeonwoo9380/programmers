def solution(x):
    answer = True
    sum = 0
    num = list(map(int, str(x)))
    for i in range(len(num)):
        sum += num[i]
    if x % sum == 0:
        return answer
    return False