def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): # len(arr1)은 [[1,2], [3, 4]]에서 [1, 2], [3, 4] 2개이다
        answer_sum = []
        for j in range(len(arr1[0])): #len(arr1[0]) [[1, 2]. [3, 4]]에서 [1, 2]의 [1], [2] 2개이다.
            answer_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_sum)
    return answer