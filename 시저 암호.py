def solution(s, n):
    answer = ''
    new = 0
    for i in range(len(s)):
        if s[i].isupper():
            new = (((ord(s[i]) - ord('A') + n) % 26) + ord('A'))
            answer += chr(new)
        elif s[i].islower():
            new = (((ord(s[i]) - ord('a') + n) % 26) + ord('a'))
            answer += chr(new)
        else:
            answer += s[i]
    return answer