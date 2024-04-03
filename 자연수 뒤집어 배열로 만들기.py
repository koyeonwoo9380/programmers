def solution(n):
    n = list(map(int, str(n)))
    answer = []
    for i in range(len(n)):
        answer.append(n[len(n)-i-1])
    return answer