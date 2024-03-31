from collections import defaultdict

def solution(tickets):
    answer = []
    graph=defaultdict(list)
    
    for src,dst in tickets:
        graph[src].append(dst)
        graph[src].sort(reverse=True)
    answer=DFS(graph,'ICN')
        
    return answer

def DFS(graph,start_node):
    need_to_visit,path =list(),list()
    need_to_visit.append(start_node)
    while need_to_visit:
        top=need_to_visit[-1]
        if graph[top]!=[]:
            need_to_visit.append(graph[top].pop())
        else:
            path.append(need_to_visit.pop())
    return path[::-1]