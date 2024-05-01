def solution(food):
    answer = ''
    for i in range(1, len(food)):
        number = int(food[i]) // 2 # 1
        answer += str(i) * number   # 'i'로 하면 i를 number 번 반복한다. str(i) =i에 해당하는 숫자 해야한다.
    answer += '0'
    # 역으로 반복
    for i in range(len(food)-1, 0, -1):  # 역순은 +1이라 0이다
        number = int(food[i]) // 2 
        answer += str(i) * number
    return answer