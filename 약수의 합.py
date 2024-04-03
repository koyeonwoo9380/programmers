def solution(n):
    answer = 0
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    for i in range(len(div)):
        answer += div[i]
    return answer