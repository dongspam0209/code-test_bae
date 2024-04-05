def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    rows = zip(range(row_begin, row_end+1), data[row_begin - 1: row_end])

    answer = 0
    for idx, row in rows:
        _sum = 0
        for element in row:
            _sum += element % idx
        answer ^= _sum

    return answer