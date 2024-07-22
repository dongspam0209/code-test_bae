# 바닥 장식

from collections import deque
# '|' '-' 으로 장식 '-'같은 행 → 한개 '|'같은 열 → 한개
# '-'용 하나랑 '|'용 하나 DFS 돌리면 될거같은데

def BFS(graph,start_x,start_y,visited):
    if visited[start_x][start_y]==True:
        return 0
    
    queue=deque([(start_x,start_y)])
    visited[start_x][start_y]=True

    if graph[start_x][start_y]=='|':
        while queue:
            cur_x,cur_y=queue.popleft()
            if cur_x+1>=N:
                continue
            if graph[cur_x+1][cur_y]=='|':
                queue.append((cur_x+1,cur_y))
                visited[cur_x+1][cur_y]=True

        return 1
    else:
        while queue:
            cur_x,cur_y=queue.popleft()
            if cur_y+1>=M:
                continue
            if graph[cur_x][cur_y+1]=='-':
                queue.append((cur_x,cur_y+1))
                visited[cur_x][cur_y+1]=True
        return 1
    

N,M=map(int,input().split())

graph=[list(input()) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
result=0

for i in range(len(graph)):
    for j in range(len(graph[0])):
        result+=BFS(graph,i,j,visited)

print(result)