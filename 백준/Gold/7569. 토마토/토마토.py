# 토마토
from collections import deque
import sys
input=sys.stdin.readline

M,N,H=map(int,input().split()) # N x M 인 상자 H개.

tomato_boxes=[[list(map(int,input().split()))for _ in range(N)]for _ in range(H)]
# 1 : 익은 토마토 0 : 익지않은 토마토 -1 : 토마토 없는 칸

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
queue=deque()

def BFS():
    while queue:
        z,x,y=queue.popleft()
        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx and nx<N and 0<=ny and ny<M and 0<=nz and nz<H:
                if tomato_boxes[nz][nx][ny]==0:
                    tomato_boxes[nz][nx][ny]=tomato_boxes[z][x][y]+1
                    queue.append((nz,nx,ny))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_boxes[i][j][k]==1:
                queue.append((i,j,k))

BFS()

impossible=False
result_day=0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_boxes[i][j][k]==0:
                impossible=True
            result_day=max(result_day,tomato_boxes[i][j][k])

if impossible:
    print(-1)
else:
    print(result_day-1)