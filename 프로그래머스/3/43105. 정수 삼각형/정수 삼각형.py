def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==(len(triangle[i])-1):
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                a=triangle[i-1][j-1]+triangle[i][j]
                b=triangle[i-1][j]+triangle[i][j]
                triangle[i][j]=max(a,b)

    answer=max(triangle[-1])
    return answer