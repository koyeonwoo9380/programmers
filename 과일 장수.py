def solution(k, m, score):
    result = 0
    group = []
    score.sort(reverse = True)
    number = len(score) // m
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            group = score[i:i+m]
            result += min(group) * m 
    return result