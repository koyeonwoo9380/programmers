def solution(a, b):
    answer = ''
    number = 0
    date = [31, 29, 31, 30, 31, 30, 31,31,30,31,30,31]
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    for i in range(a):
        if (i+1) == a:
            break
        number += int(date[i])
    number += b
    answer = day[number % 7]
    return answer