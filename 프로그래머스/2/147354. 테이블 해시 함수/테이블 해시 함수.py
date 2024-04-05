def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col-1],-x[0]))
    answer=0
    
    for idx in range(row_begin-1,row_end):
        S=0
        for j in range(len(data[idx])):
            S+=data[idx][j]%(idx+1)
        answer^=S
    
    return answer

    