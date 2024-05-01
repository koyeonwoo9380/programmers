def solution(strings, n):
    strings.sort()  # n번째 글자가 동일한 경우 우선순위를 못하니까 미리 내림차순
    answer = sorted(strings, key=lambda x:x[n])  # key값에 x[n]을 줘서 key값으로 내림차순
    return answer