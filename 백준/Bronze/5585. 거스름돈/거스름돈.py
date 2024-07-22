n=int(input())
a=[500,100,50,10,5,1]
change=1000-n
count=0
for coin in a:
    count+=change//coin
    change%=coin

print(count)