def solution(s, skip, index):
    answer = ''
    ch='abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        if i in ch:
            ch = ch.replace(i,"")
    for j in s:
        change = ch[(ch.index(j)+index) % len(ch)]
        answer += change
    return answer