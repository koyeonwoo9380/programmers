def solution(cards1, cards2, goal):
    answer = ''
    g1 = []
    g2 = []
    for i in goal:
        if cards1 and cards1[0] == i:  #i는 goal의 단어이다. / cards1은 리스트가 없는 경우 pass, 리스트나 튜플, 문자열 등의 시퀀스에서 존재하지 않는 인덱스에 접근할 때. 인덱스를 사용하여 요소를 변경하거나 삭제할 때 리스트의 범위를 벗어나는 경우.
            cards1.pop(0)
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'
        