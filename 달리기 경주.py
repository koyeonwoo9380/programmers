def solution(players, callings):
    answer = []
    dic = {}
    for rank, name in enumerate(players):
        dic[name] = rank
    for name in callings:
        idx = dic[name]
        dic[name] -= 1
        dic[players[idx-1]] += 1
        players[idx-1],players[idx] = players[idx], players[idx-1]
    
    return players