def solution(number, limit, power):
    answer = 0
    measure = []
    count = 0
    for i in range(1, number+1):
        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                count += 1
                if i != j**2:
                    count +=1  # 약수 개수 구하는 틀 (다른건 시간 복잡도 크다)
        measure.append(count)
        count =0
    for i in range(len(measure)):
        if measure[i] > limit:
            measure[i] = power
        answer += measure[i]
    return answer