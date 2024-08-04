# 시리얼 번호
N=int(input())
guitar_list=[input() for _ in range(N)]

def check_number(string):
    number_sum=0
    for char in string:
        if char.isdigit():
            number_sum+=int(char)
            
    return number_sum
        

guitar_list.sort(key=lambda x : (len(x),check_number(x),x))



for ans in guitar_list:
    print(ans)