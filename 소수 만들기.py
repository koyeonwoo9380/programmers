import itertools
def is_prime(num):
    prime = True
    answer = 0
    if num == 0 or num == 1:
        prime = False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
            break
    return True
def solution(nums):
    result = 0
    sum1 = 0
    ncr = list(itertools.combinations(nums,3))
    for combo in ncr:
        sum1 = sum(combo)
        if is_prime(sum1):
            result += 1
    return result