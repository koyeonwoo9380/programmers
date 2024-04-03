def solution(price, money, count):
    answer = 0
    sum1 = 0
    for i in range(count):
        sum1 += price * (i+1) 
    answer = sum1 - money
    if answer <= 0:
        return 0
    return answer