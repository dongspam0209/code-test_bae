# 문자열
import sys
min_size=sys.maxsize
A,B=input().split()

# 이미 있는 문자열에서 최소가 되는 상황 구한 후, 앞이나 뒤에 추가해서 완성.
# 사실 길이가 달라도 상관이 없어, 현재 있는 상황에서 다른것만 count하면 됨


for i in range(len(B)):
    count=0
    for j in range(len(A)):
        if i+len(A)>len(B):
            count=sys.maxsize
            break # 나중에 해결

        if A[j]!=B[i+j]:
            count+=1
            
    min_size=min(count,min_size)

print(min_size)