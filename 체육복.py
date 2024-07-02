def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    answer = n - len(lost_set)
    for i in sorted(lost_set):
        if (i-1) in reserve_set:
            answer += 1
            reserve_set.remove(i-1)
        elif (i+1) in reserve_set:
            answer += 1
            reserve_set.remove(i+1)
    return answer