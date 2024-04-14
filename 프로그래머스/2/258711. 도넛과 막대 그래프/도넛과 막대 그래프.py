def solution(edges):
    answer = [0,0,0,0]
    node_dict=dict()
    for src,dst in edges:
        if not node_dict.get(src):
            node_dict[src]=[0,0]
        if not node_dict.get(dst):
            node_dict[dst]=[0,0]
        
        node_dict[src][0]+=1
        node_dict[dst][1]+=1
    for node,cnt in node_dict.items():
        if cnt[1]==0 and cnt[0]>=2:
            answer[0]=node
        elif cnt[0]==0 and cnt[1]>0:
            answer[2]+=1
        elif cnt[0]>=2 and cnt[1]>=2:
            answer[3]+=1
        
    answer[1]= node_dict[answer[0]][0]-answer[2]-answer[3]
    
    return answer