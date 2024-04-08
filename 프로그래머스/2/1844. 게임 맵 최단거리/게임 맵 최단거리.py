from collections import deque
def solution(maps):
    answer = 0
    answer=BFS(maps,0,0,len(maps)-1,len(maps[0])-1)
    return answer

def BFS(graph,start_x,start_y,end_x,end_y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(graph)
    m=len(graph[0])
    visited=set([(start_x,start_y)])
    queue=deque([(start_x,start_y,[(start_x,start_y)])])
    count=0
    while queue:
        curr_x,curr_y,path =queue.popleft()
        # print((curr_x,curr_y))
        for idx in range(4):
            nx=curr_x+dx[idx]
            ny=curr_y+dy[idx]
            if nx==end_x and ny==end_y:
                return len(path)+1
            
            if 0<=nx<n and 0<=ny<m:
                if(nx,ny) not in visited:
                    if graph[nx][ny]==1:
                        visited.add((nx,ny))
                        queue.append((nx,ny,path+[(nx,ny)]))
                        count+=1
    return -1