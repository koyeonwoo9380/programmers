def solution(arr):
    k = 0
    if len(arr) == 1:
        arr = [-1]
        return arr
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
            k = i
    arr.pop(k)
    return arr