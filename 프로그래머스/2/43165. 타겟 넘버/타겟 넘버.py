from itertools import product
def solution(numbers, target):
    num_with_sign=[(x,-x)for x in numbers]
    all_case= list(map(sum,product(*num_with_sign)))
    
    
    return all_case.count(target)