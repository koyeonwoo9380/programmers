def solution(s):
    answer = []
    word = {}  # 딕션어리로 풀기
    for i in range(len(s)):
        if s[i] in word:
            answer.append(i - word[s[i]])
            word[s[i]] = i  # 딕션어리의 key에 value값 정의
        else:
            answer.append(-1)
            word[s[i]] = i
    return answer