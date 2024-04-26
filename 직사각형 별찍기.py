a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a, end='\n')  # '문자' * 숫자 => 문자를 숫자만큼 반복, 줄바꿈