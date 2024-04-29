def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)): # range범위가 1부터가 아니라 i+1이다.
            for k in range(j+1, len(number)): # range범위가 2부터가 아니라 j+1이다.
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer