# 단지번호붙이기
N=int(input())
graph=[list(input()) for _ in range(N)]

path=[]

def DFS(graph,cur_i,cur_j):
    dx_list=[-1,1,0,0]
    dy_list=[0,0,-1,1]

    graph[cur_i][cur_j]="0"
    
    path.append((cur_i,cur_j))
    for dx,dy in zip(dx_list,dy_list):
        if cur_i+dx >= N or cur_j+dy>=N or cur_i+dx<0 or cur_j+dy<0 : 
            continue
        if graph[cur_i+dx][cur_j+dy]== "1":
            DFS(graph,cur_i+dx,cur_j+dy)

    cnt=len(path)
    
    return cnt

house_list=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]=="1":
            house_list.append(DFS(graph,i,j))
            path=[]

print(len(house_list))
house_list.sort()
for house_area in house_list:
    print(house_area)