# 바이러스
from collections import defaultdict,deque
N=int(input())
E=int(input()) # 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수
graph=defaultdict(list)

for i in range(E):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def BFS(graph,start):
    queue=deque([start])
    visited=[]

    while queue:
        cur_node=queue.popleft()
        visited.append(cur_node)
        for next_node in graph[cur_node]:
            if next_node not in visited:
                queue.append(next_node)
                
    visited=set(visited)
    print(len(visited)-1)

BFS(graph=graph,start=1)

