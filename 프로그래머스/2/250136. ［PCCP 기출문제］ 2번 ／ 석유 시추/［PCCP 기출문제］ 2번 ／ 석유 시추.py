from collections import deque
def solution(land):
    answer = 0
    visited=[[0 for i in range(len(land[0]))] for j in range(len(land))]
    result=[0 for i in range(len(land[0])+1)]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if visited[i][j]==0 and land[i][j]==1:
                BFS(i,j,land,visited,result)
                
    answer=max(result)
    return answer
    
def BFS(start_x,start_y,graph,visited,result):
        count=0
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        queue=deque([(start_x,start_y)])
        min_y,max_y=start_y,start_y
        visited[start_x][start_y]=1
        while queue:
            x,y=queue.popleft()
            min_y=min(min_y,y)
            max_y=max(max_y,y)
            count+=1
            for idx in range(4):
                #idx:0 (x-1,y) idx:1 (x+1,y) idx:2 (x,y-1) idx:3 (x,y+1)
                nx= x+dx[idx]
                ny= y+dy[idx]
                if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]):
                    continue
                if visited[nx][ny]==0 and graph[nx][ny]==1:
                    visited[nx][ny]=1
                    queue.append((nx,ny))
                    
        for idx in range(min_y,max_y+1):
            result[idx]+=count   
