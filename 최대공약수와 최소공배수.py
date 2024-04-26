def solution(n, m):
    answer = []
    if n < m:
        k = n
    else:
        k = m
    for i in range(1, k+1):
        if (n % i ==0) and (m % i ==0): # 최대공약수
            max_divisor = i
        min_multi = max_divisor * (n // max_divisor) * (m // max_divisor)  # 최소공배수
    answer.append(max_divisor)
    answer.append(min_multi)
    return answer