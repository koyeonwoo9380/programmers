#case 1
def solution(s):
    s = sorted(s, reverse = True) # sorted는 새로운 '리스트로' 반환
    answer = ''.join(s)
    return answer

# case2
def solution(s):
    s = list(s)
    s.sort(reverse=True)  # sort는 반환 x
    answer = ''.join(s)
    return answer