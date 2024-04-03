def solution(a, b):
    if a < b:
        answer = a + b
        for i in range(a+1,b):
            answer += i
        return answer
    elif a > b:
        answer = a + b
        for i in range(b+1,a):
            answer += i
        return answer
    else:
        return a