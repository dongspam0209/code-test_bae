from collections import defaultdict
import math

def hour_2_min(time):
    hour=int(time[:2])
    minute=int(time[3:])
    
    return hour*60+minute

def solution(fees, records):
    dict_park={}
    fin_dict_park=defaultdict(int)
    answer = []
    
    for idx in range(len(records)):
        temp_time,car_num,status=records[idx].split()
        
        time=hour_2_min(temp_time)
        
        if status=='IN':
            dict_park[car_num]=time
        else:
            old_time=dict_park[car_num]
            parked_time=time-old_time
            del dict_park[car_num]
            
            fin_dict_park[car_num]+=parked_time
    
    remain_car_num=list(dict_park.keys())
    
    for car_num in remain_car_num:
        old_time=dict_park[car_num]
        parked_time=1439-old_time
        del dict_park[car_num]
        
        fin_dict_park[car_num]+=parked_time
    
    fin_dict_park=dict(sorted(fin_dict_park.items()))
    arr=fin_dict_park.values()
    for time in arr:
        if time>fees[0]:
            fee=fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]
        else:
            fee=fees[1]
        
        answer.append(fee)
    return answer