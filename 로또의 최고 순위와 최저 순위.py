def solution(lottos, win_nums):
    answer = []
    win = 0
    num = 0
    for i in lottos:
        if i == 0:
            num += 1
        else:
            for j in win_nums:
                if i == j:
                    win += 1
    maxi = win + num
    mini = win 
    rank = {6:1,5:2, 4:3, 3:4,2:5,1:6, 0:6}
    answer = [rank[maxi], rank[mini]]
    return answer