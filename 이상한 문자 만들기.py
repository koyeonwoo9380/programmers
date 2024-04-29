def solution(s):
    k = 0
    answer = ""
    for i in range(len(s)):
        if s[k] == " ":
            answer += " "
            k += 1 
        else:
            if k % 2 == 0:
                answer += s[k].upper()
                k += 1 
            else:
                answer += s[k]
                k += 1
    return answer