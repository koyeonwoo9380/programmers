def solution(s):
    answer = ""
    word = ""
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            word += s[i]
            if word == "one":
                answer += '1'
            elif word == "two":
                answer += '2'
            elif word == "three":
                answer += str(3)
            elif word == "four":
                answer += '4'
            elif word == "five":
                answer += str(5)
            elif word == "six":
                answer += str(6)
            elif word == "seven":
                answer += '7'
            elif word == "eight":
                answer += '8'
            elif word == "nine":
                answer += str(9)
            elif word == "zero":
                answer += '0'
            if word in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]:
                word = ""
    return int(answer)