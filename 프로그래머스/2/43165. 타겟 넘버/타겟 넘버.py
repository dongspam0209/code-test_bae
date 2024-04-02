from collections import defaultdict
global path
path=list()

def solution(numbers, target):
    answer = 0
    numbers_with_sign=list()
    number_graph=defaultdict(list)
    
    for number in numbers:
        pos_neg=[number,-number]
        numbers_with_sign.extend(pos_neg)
        
    for idx in range(0,len(numbers_with_sign)-2,2):
        idx_list=[idx+2,idx+3]
        number_graph[idx].extend(idx_list)
        number_graph[idx+1].extend(idx_list)
    
    DFS(number_graph,0,len(numbers_with_sign)-2,numbers_with_sign,target)
    DFS(number_graph,0,len(numbers_with_sign)-1,numbers_with_sign,target)
    DFS(number_graph,1,len(numbers_with_sign)-2,numbers_with_sign,target)
    DFS(number_graph,1,len(numbers_with_sign)-1,numbers_with_sign,target)
    
    answer=len(path)
    
    
    return answer

def DFS(graph,start,end,nums_with_sign,target,visited=[]):
    visited=visited+[start]
    if start==end:
        sum_list=list()
        for idx in visited:
            sum_list.append(nums_with_sign[idx])
        if target==sum(sum_list):
            path.append(visited)
        
    for node in graph[start]:
        if node not in visited:
            DFS(graph,node,end,nums_with_sign,target,visited)
            

    return path
