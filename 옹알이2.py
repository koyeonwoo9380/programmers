def solution(babbling):
    answer = 0
    for i in babbling:
        for word in [ "aya", "ye", "woo", "ma"]:
            if word * 2 not in i:
                i = i.replace(word, "")
        if len(i) == 0:
            answer += 1
    return answer