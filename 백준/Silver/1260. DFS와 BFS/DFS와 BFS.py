from collections import defaultdict,deque
N,M,V=map(int,input().split())
graph=defaultdict(list)
for _ in range(M):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def DFS(graph,start_node):
    need_visit,visited=list(),list()
    need_visit.append(start_node)
    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            visited.append(node)
            graph[node].sort(reverse=True)
            need_visit.extend(graph[node])
            
    return visited

def BFS(graph,start_node):
    queue=deque([start_node])
    visited=[start_node]
    while queue:
        curr_node=queue.popleft()
        graph[curr_node].sort()
        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
                
    return visited

dfs=DFS(graph,V)
bfs=BFS(graph,V)

for i in dfs:
    print(i,end=" ")
print()
for j in bfs:
    print(j,end=" ")