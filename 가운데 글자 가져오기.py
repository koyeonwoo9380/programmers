def solution(s):
    # word = list(map(int ,s)) 문자열은 자동으로 리스트여서 바꿀 필요가 없다.
    for i in range(len(s)):
        if len(s) % 2 == 0:
            answer = s[(len(s)) // 2 -1] + s[(len(s)) // 2]
        else:
            answer = s[(len(s)) // 2]
    return answer