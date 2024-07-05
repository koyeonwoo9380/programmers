def solution(keymap, targets):
    answer = []
    times = {}
    for key in keymap:
        for idx, alpha in enumerate(key):
            if alpha in times.keys():
                if times[alpha] > idx + 1:
                    times[alpha] = idx + 1
            else:
                times[alpha] = idx + 1
    
    for goal in targets:
        result = 0
        for alpha in goal:
            if alpha in times:
                result += times[alpha]
            else:
                result = -1
                break
        answer.append(result)
    return answer