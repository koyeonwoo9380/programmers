def solution(name, yearning, photo):
    answer = []
    score = 0
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j] == name[k]:
                    score += yearning[k]
        answer.append(score)
        score = 0
    return answer