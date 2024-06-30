def solution(N, stages):
    answer = []
    ratio = {}
    players = len(stages)
    
    for i in range(1, N + 1):
        if players > 0:
            count = stages.count(i)
            ratio[i] = count / players
            players -= count
        else:
            ratio[i] = 0
    
    answer = sorted(ratio, key=lambda x: ratio[x], reverse=True)
    
    return answer