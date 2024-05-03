def solution(answers):
    answer = [0 for i in range(3)]
    first = [ 1, 2, 3, 4, 5]
    second=[2, 1, 2, 3, 2, 4, 2, 5]
    third=[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    for i in range(len(answers)):
        if first[(i%len(first))] == answers[i]: # len(answers)가 len(first)보다 길면 first[i]초과 그래서 반복하기 위해서 %를 쓴다. 
            answer[0] += 1
        if second[(i%len(second))] == answers[i]: # elif는 if문이 맞으면 건너뛰는데 if를 써서 또 맞는지 확인한다.
            answer[1] += 1
        if third[(i%len(third))] == answers[i]:
            answer[2] += 1
    for j in range(len(answer)):
        if answer[j] == max(answer): # list의 max값
            result.append(j+1)
    return result