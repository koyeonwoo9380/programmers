def solution(array, commands):
    answer = []
    cut = []
    for i in range(len(commands)):
        first = commands[i][0] -1
        second = commands[i][1]
        third = commands[i][2] -1
        cut = array[first:second]
        cut.sort()
        answer.append(cut[third])
        cut=[]
    return answer