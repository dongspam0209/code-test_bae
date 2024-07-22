N=int(input())
P=list(map(int,input().split()))

P.sort()

wait_time=[]
for idx in range(len(P)):
    weighted_wait_time=sum(P[:idx])
    wait_time.append(weighted_wait_time+P[idx])


print(sum(wait_time))