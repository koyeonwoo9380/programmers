def solution(s):
    answer = ""
    word = s.split(" ")  # 띄어쓰기로 나눈다. 즉 단어마다 나눈다.
    for i in word:   # for i in range(숫자) range 뒤에는 숫자가 나와야 해서 range안쓰고 word를 썼다. 
        for j in range(len(i)):  # 단어의 글자 수만큼 반복
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "       # for문이 끝나면 = 한 단어가 끝나면 " "띄어쓰기로
    return answer[:-1]