N,M=map(int,input().split())
A=list(map(int,input().split()))
start=0
end=1
count=0
sum=A[0]
while True:
    if sum<M:
        if end<N:
            sum+=A[end]
            end+=1
        else:
            break
    elif sum==M:
        count+=1
        sum-=A[start]
        start+=1
    else:
        sum-=A[start]
        start+=1
print(count)