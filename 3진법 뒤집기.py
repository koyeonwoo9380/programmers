def solution(n):
    answer = ""
    while n > 0:
        answer += str(n % 3) # x진법= x로 나눠서 나머지이다. 나중에 나눈 나머지가 가장 숫자이다. 
        n = n // 3
    return int(answer, 3)