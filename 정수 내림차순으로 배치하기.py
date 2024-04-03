def solution(n):
    answer = 0
    n = list(map(int, str(n)))
    n.sort(reverse = True)
    for i in range(len(n)):
        answer += n[i] * (10 ** (len(n)-1-i))
    return answer