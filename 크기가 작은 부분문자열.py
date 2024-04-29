def solution(t, p):
    answer = 0
    number = ''
    for i in range(len(t)-len(p)+1):
        number = t[i:i+len(p)]
        if int(number) <= int(p):
            answer += 1
    return answer