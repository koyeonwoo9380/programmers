def solution(left, right):
    sum1 = 0
    for i in range(left, right+1):
        answer = 0   # 여기서 초기화를 해야돼. 그래야 i값이 1씩 증가할 때마다 약수의 개수도 초기화
        for k in range(1, i+1):
            if i % k == 0:
                answer += 1
        if answer % 2 == 0:
            sum1 += i
        else:
            sum1 -= i
    return sum1