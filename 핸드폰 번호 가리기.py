def solution(phone_number):
    answer = list(map(str, phone_number))  # *를 붙여야 하니까 str로 변환
    for i in range(len(answer)-4):
        answer[i] = '*'
    answer = ''.join(answer) # 리스트를 정수로 변환
    return answer