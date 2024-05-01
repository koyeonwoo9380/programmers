def solution(a, b, n):
    answer = 0
    while (n >= a):
        first = n // a
        answer += first * b
        n = (n % a) + (first*b)
    return answer