def solution(num_list):
    answer = []
    num_list.sort()
    for idx in range (5,len(num_list)):
        answer.append(num_list[idx])
    return answer