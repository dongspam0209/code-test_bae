# 로봇 청소기
# 각 칸은 벽 또는 빈 칸 처음 빈 칸은 전부 청소되지 않은 상태
# d : 0-N 1-E 2-S 3-W
N,M=map(int,input().split())
r,c,d=map(int,input().split())

room=[list(map(int,input().split())) for _ in range(N)]

def clean_agent(room,current_x,current_y,direction):
    count=0
    while current_x<N and current_x>=0 and current_y<M and current_y>=0:

        if room[current_x][current_y]==0: # 현재 위치가 청소되지 않은 경우, 현재 칸 청소 (count +1 room 2로 바꿈)
            count+=1
            room[current_x][current_y]=2
        
        if room[current_x-1][current_y]!=0 and room[current_x+1][current_y]!=0 and room[current_x][current_y-1]!=0 and room[current_x][current_y+1]!=0:
            if direction==0: # N 바라본 청소기
                if room[current_x+1][current_y]==1:
                    break
                current_x,current_y=current_x+1,current_y
                continue

            elif direction==1: # E 바라본 청소기
                if room[current_x][current_y-1]==1:
                    break
                current_x,current_y=current_x,current_y-1
                continue
                
            elif direction==2: # S 바라본 청소기
                if room[current_x-1][current_y]==1:
                    break
                current_x,current_y=current_x-1,current_y
                continue
                
            elif direction==3: # W 바라본 청소기
                if room[current_x][current_y+1]==1:
                    break
                current_x,current_y=current_x,current_y+1
                continue
        else:
            # 0→3→2→1→0 90도 회전
            if direction==0:
                direction=3
            else:
                direction-=1
            
            if direction==0: # N 바라본 청소기
                if room[current_x-1][current_y]==0:
                    current_x,current_y=current_x-1,current_y
                    continue

            elif direction==1: # E 바라본 청소기
                if room[current_x][current_y+1]==0:
                    current_x,current_y=current_x,current_y+1
                    continue
                
            elif direction==2: # S 바라본 청소기
                if room[current_x+1][current_y]==0:
                    current_x,current_y=current_x+1,current_y
                    continue
                
            elif direction==3: # W 바라본 청소기
                if room[current_x][current_y-1]==0:
                    current_x,current_y=current_x,current_y-1
                    continue
    return count

print(clean_agent(room,r,c,d))