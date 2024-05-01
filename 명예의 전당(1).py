def solution(k, score):
    answer = []
    top_score = []
    for i in range(len(score)):
        if len(top_score) == k:
            if top_score[0] <= score[i]:
                top_score.pop(0)
                top_score.append(score[i])
                top_score.sort()
                answer.append(top_score[0])
            else:
                answer.append(top_score[0])
            
        else:
            top_score.append(score[i])
            top_score.sort()
            answer.append(top_score[0])
    return answer