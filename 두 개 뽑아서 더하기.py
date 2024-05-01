def solution(numbers):
    answer = set() # 중복된걸 버릴려면 set
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer