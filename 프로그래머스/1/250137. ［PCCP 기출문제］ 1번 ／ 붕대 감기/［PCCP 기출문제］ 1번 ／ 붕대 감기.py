def solution(bandage, health, attacks):
    cur_health=health
    max_health=health
    idx=0
    success=0
    answer = 0
    
    for t in range(attacks[-1][0]+1):
        if t==attacks[idx][0]:
            cur_health-=attacks[idx][1]
            success=0
            idx+=1
            if cur_health<=0:
                answer=-1
                
                return answer
            else:
                continue;
        else:
            cur_health+=bandage[1]
            if t==0:
                success=0
            else:
                success+=1
            if success==bandage[0]:
                cur_health+=bandage[2]
                success=0
            if cur_health>=max_health:
                cur_health=max_health        

    answer=cur_health
    return answer