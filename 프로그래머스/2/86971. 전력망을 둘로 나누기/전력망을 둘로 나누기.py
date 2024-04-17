from collections import deque,defaultdict
def solution(n, wires):
    answer = -1
    graph=defaultdict(list)
    node_count_list=list()
    for src,dst in wires:
        graph[src].append(dst)
        graph[dst].append(src)
    for src,dst in wires:
        node_count_list.append(abs(BFS(graph,dst,src)-BFS(graph,src,dst)))

    answer=min(node_count_list)
    return answer

def BFS(graph,start_node,impossible_next_node):
    queue=deque([start_node])
    visited=set([start_node])
    count=0
    while queue:
        curr_node=queue.popleft()
        count+=1
        for next_node in graph[curr_node]:
            if next_node not in visited and next_node!=impossible_next_node:
                visited.add(next_node)
                queue.append(next_node)
                
    return count