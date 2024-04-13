import sys
input=sys.stdin.readline
N, M = map(int, input().split())

a = [int(input()) for _ in range(N)]
    
a.sort()
start=0
end=0
answer=2000000000
while end<N:
    diff=a[end]-a[start]
    if M > diff:
        end+=1
    elif diff>M:
        answer=min(diff,answer)
        start+=1
    else:
        answer=M
        break

print(answer)