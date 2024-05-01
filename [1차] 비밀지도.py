def solution(n, arr1, arr2):
    answer = []
    word = ''
    for i in range(len(arr1)):
        a = arr1[i]|arr2[i] 
        b = bin(a)[2:].zfill(n)  # n칸이 안되면 왼쪽에 0으로 채운다, bin으로 2진법으로 바꾸면 리스트 형태로 변한다. [2:]은 앞에 0b를 버린다.
        for j in range(n):
            if a[j] == '1':
                word += '#'
            else:
                word += ' '
        answer.append(word)
    word = ''
    return answer