def solution(s):
    answer = True
    p = 0
    y = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
    if p != y:
        return False
    return True